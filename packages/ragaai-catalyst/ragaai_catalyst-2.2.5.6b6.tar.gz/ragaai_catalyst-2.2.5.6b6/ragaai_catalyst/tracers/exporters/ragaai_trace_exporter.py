import json
import logging
import os
import tempfile
from dataclasses import asdict
from typing import Optional, Callable, Dict, List

from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult

from ragaai_catalyst.tracers.agentic_tracing.upload.trace_uploader import (
    submit_upload_task,
)
from ragaai_catalyst.tracers.agentic_tracing.utils.system_monitor import SystemMonitor
from ragaai_catalyst.tracers.agentic_tracing.utils.trace_utils import (
    format_interactions,
)
from ragaai_catalyst.tracers.agentic_tracing.utils.zip_list_of_unique_files import (
    zip_list_of_unique_files,
)
from ragaai_catalyst.tracers.utils.trace_json_converter import convert_json_format

logger = logging.getLogger("RagaAICatalyst")
logging_level = (
    logger.setLevel(logging.DEBUG) if os.getenv("DEBUG") == "1" else logging.INFO
)


class TracerJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, bytes):
            try:
                return obj.decode("utf-8")
            except UnicodeDecodeError:
                return str(obj)  # Fallback to string representation
        if hasattr(obj, "to_dict"):  # Handle objects with to_dict method
            return obj.to_dict()
        if hasattr(obj, "__dict__"):
            # Filter out None values and handle nested serialization
            return {
                k: v
                for k, v in obj.__dict__.items()
                if v is not None and not k.startswith("_")
            }
        try:
            # Try to convert to a basic type
            return str(obj)
        except:
            return None  # Last resort: return None instead of failing


class RAGATraceExporter(SpanExporter):
    def __init__(
            self,
            project_name: str,
            dataset_name: str,
            base_url: str,
            tracer_type: str,
            files_to_zip: Optional[List[str]] = None,
            project_id: Optional[str] = None,
            user_details: Optional[Dict] = None,
            custom_model_cost: Optional[dict] = None,
            timeout: int = 120,
            post_processor: Optional[Callable] = None,
            max_upload_workers: int = 30,
            user_context: Optional[str] = None,
            user_gt: Optional[str] = None,
            external_id: Optional[str] = None
    ):
        self.trace_spans = dict()
        # Use custom trace directory if environment variable is set, otherwise use temp directory
        custom_dir = os.getenv("RAGAAI_TRACE_DIR")
        if custom_dir:
            try:
                # Create the directory if it doesn't exist
                os.makedirs(custom_dir, exist_ok=True)
                self.tmp_dir = custom_dir
                logger.info(f"Using custom trace directory: {custom_dir}")
            except Exception as e:
                logger.warning(f"Error with custom trace directory {custom_dir}: {e}")
                logger.info("Falling back to temp directory")
                self.tmp_dir = tempfile.gettempdir()
        else:
            self.tmp_dir = tempfile.gettempdir()
            logger.info(f"Using temp directory: {self.tmp_dir}")
            
        self.tracer_type = tracer_type
        self.files_to_zip = files_to_zip
        self.project_name = project_name
        self.project_id = project_id
        self.dataset_name = dataset_name
        self.user_details = user_details
        self.base_url = base_url
        self.custom_model_cost = custom_model_cost
        self.system_monitor = SystemMonitor(dataset_name)
        self.timeout = timeout
        self.post_processor = post_processor
        self.max_upload_workers = max_upload_workers
        self.user_context = user_context
        self.user_gt = user_gt
        self.external_id = external_id

    def export(self, spans):
        for span in spans:
            try:
                span_json = json.loads(span.to_json())
                trace_id = span_json.get("context").get("trace_id")
                if trace_id is None:
                    logger.error("Trace ID is None")

                if trace_id not in self.trace_spans:
                    self.trace_spans[trace_id] = list()

                if span_json.get("attributes").get("openinference.span.kind", None) is None:
                    span_json["attributes"]["openinference.span.kind"] = "UNKNOWN"

                self.trace_spans[trace_id].append(span_json)

                if span_json["parent_id"] is None:
                    trace = self.trace_spans[trace_id]
                    try:
                        self.process_complete_trace(trace, trace_id)
                    except Exception as e:
                        logger.error(f"Error processing complete trace: {e}")
                    try:
                        del self.trace_spans[trace_id]
                    except Exception as e:
                        logger.error(f"Error deleting trace: {e}")
            except Exception as e:
                logger.warning(f"Error processing span: {e}")
                continue

        return SpanExportResult.SUCCESS

    def shutdown(self):
        # Process any remaining traces during shutdown
        logger.debug("Reached shutdown of exporter")
        for trace_id, spans in self.trace_spans.items():
            self.process_complete_trace(spans, trace_id)
        self.trace_spans.clear()

    def process_complete_trace(self, spans, trace_id):
        # Convert the trace to ragaai trace format
        try:
            ragaai_trace_details = self.prepare_trace(spans, trace_id)
        except Exception as e:
            print(f"Error converting trace {trace_id}: {e}")
            return  # Exit early if conversion fails

        # Check if trace details are None (conversion failed)
        if ragaai_trace_details is None:
            logger.error(f"Cannot upload trace {trace_id}: conversion failed and returned None")
            return  # Exit early if conversion failed

        # Upload the trace if upload_trace function is provided
        try:
            if self.post_processor != None:
                ragaai_trace_details['trace_file_path'] = self.post_processor(ragaai_trace_details['trace_file_path'])
            self.upload_trace(ragaai_trace_details, trace_id)
        except Exception as e:
            print(f"Error uploading trace {trace_id}: {e}")

    def prepare_trace(self, spans, trace_id):
        try:
            # Extract external_id from spans via OpenInference user.id (prefer root span)
            external_id_from_spans = None
            try:
                root_span = next((s for s in spans if s.get("parent_id") is None), None)
                if root_span:
                    external_id_from_spans = (
                        root_span.get("attributes", {}).get("user.id")
                    )
                if not external_id_from_spans:
                    for s in spans:
                        external_id_from_spans = s.get("attributes", {}).get("user.id")
                        if external_id_from_spans:
                            break
            except Exception:
                external_id_from_spans = None

            try:
                ragaai_trace = convert_json_format(
                    spans,
                    self.custom_model_cost,
                    self.user_context,
                    self.user_gt,
                    external_id_from_spans if external_id_from_spans else self.external_id,
                )
            except Exception as e:
                print(f"Error in convert_json_format function: {trace_id}: {e}")
                return None

            try:
                interactions = format_interactions(ragaai_trace)
                ragaai_trace["workflow"] = interactions['workflow']
            except Exception as e:
                print(f"Error in format_interactions function: {trace_id}: {e}")
                return None

            try:
                # Add source code hash
                hash_id, zip_path = zip_list_of_unique_files(
                    self.files_to_zip, output_dir=self.tmp_dir
                )
            except Exception as e:
                print(f"Error in zip_list_of_unique_files function: {trace_id}: {e}")
                return None

            try:
                ragaai_trace["metadata"]["system_info"] = asdict(self.system_monitor.get_system_info())
                ragaai_trace["metadata"]["resources"] = asdict(self.system_monitor.get_resources())
            except Exception as e:
                print(f"Error in get_system_info or get_resources function: {trace_id}: {e}")
                return None

            try:
                ragaai_trace["metadata"]["system_info"]["source_code"] = hash_id
            except Exception as e:
                print(f"Error in adding source code hash: {trace_id}: {e}")
                return None

            try:
                ragaai_trace["data"][0]["start_time"] = ragaai_trace["start_time"]
                ragaai_trace["data"][0]["end_time"] = ragaai_trace["end_time"]
            except Exception as e:
                print(f"Error in adding start_time or end_time: {trace_id}: {e}")
                return None

            try:
                ragaai_trace["project_name"] = self.project_name
            except Exception as e:
                print(f"Error in adding project name: {trace_id}: {e}")
                return None

            try:
                # Add tracer type to the trace
                ragaai_trace["tracer_type"] = self.tracer_type
            except Exception as e:
                print(f"Error in adding tracer type: {trace_id}: {e}")
                return None

            # Add user passed metadata to the trace
            try:
                logger.debug("Started adding user passed metadata")

                metadata = (
                    self.user_details.get("trace_user_detail", {}).get("metadata", {})
                    if self.user_details else {}
                )

                if isinstance(metadata, dict):
                    for key, value in metadata.items():
                        if key not in {"log_source", "recorded_on"}:
                            ragaai_trace.setdefault("metadata", {})[key] = value

                logger.debug("Completed adding user passed metadata")
            except Exception as e:
                print(f"Error in adding metadata: {trace_id}: {e}")
                return None

            try:
                # Save the trace_json 
                trace_file_path = os.path.join(self.tmp_dir, f"{trace_id}.json")
                with open(trace_file_path, "w") as file:
                    json.dump(ragaai_trace, file, cls=TracerJSONEncoder, indent=2)
            except Exception as e:
                print(f"Error in saving trace json: {trace_id}: {e}")
                return None

            return {
                'trace_file_path': trace_file_path,
                'code_zip_path': zip_path,
                'hash_id': hash_id
            }
        except Exception as e:
            print(f"Error converting trace {trace_id}: {str(e)}")
            return None

    def upload_trace(self, ragaai_trace_details, trace_id):
        filepath = ragaai_trace_details['trace_file_path']
        hash_id = ragaai_trace_details['hash_id']
        zip_path = ragaai_trace_details['code_zip_path']
        self.upload_task_id = submit_upload_task(
            filepath=filepath,
            hash_id=hash_id,
            zip_path=zip_path,
            project_name=self.project_name,
            project_id=self.project_id,
            dataset_name=self.dataset_name,
            user_details=self.user_details,
            base_url=self.base_url,
            tracer_type=self.tracer_type,
            timeout=self.timeout
        )

        logger.info(f"Submitted upload task with ID: {self.upload_task_id}")
