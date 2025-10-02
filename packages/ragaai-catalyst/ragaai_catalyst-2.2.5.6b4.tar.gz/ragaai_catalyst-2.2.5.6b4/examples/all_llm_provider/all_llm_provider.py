import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from openai import OpenAI, AsyncOpenAI, AzureOpenAI, AsyncAzureOpenAI
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
import google.generativeai as genai
from litellm import completion, acompletion
import litellm
import anthropic
from anthropic import Anthropic, AsyncAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from groq import Groq, AsyncGroq

from ragaai_catalyst import trace_llm

from dotenv import load_dotenv
load_dotenv()

# Azure OpenAI setup
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")

# Google AI setup
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Vertex AI setup
vertexai.init(project="gen-lang-client-0655603261", location="us-central1")

async def get_llm_response(
    prompt,
    model, 
    provider,
    temperature,
    max_tokens,
    async_llm=False,
    ):
    """
    Main interface for getting responses from various LLM providers
    """
    if 'azure' in provider.lower():
        if async_llm:
            async_azure_openai_client = AsyncAzureOpenAI(azure_endpoint=azure_endpoint, api_key=azure_api_key, api_version=azure_api_version)
            return await _get_async_azure_openai_response(async_azure_openai_client, prompt, model, temperature, max_tokens)
        else:
            azure_openai_client = AzureOpenAI(azure_endpoint=azure_endpoint, api_key=azure_api_key, api_version=azure_api_version)
            return _get_azure_openai_response(azure_openai_client, prompt, model, temperature, max_tokens)
    elif 'openai_beta' in provider.lower():
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        return _get_openai_beta_response(openai_client, prompt, model, temperature, max_tokens)
    elif 'openai' in provider.lower():
        if async_llm:
            async_openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            return await _get_async_openai_response(async_openai_client, prompt, model, temperature, max_tokens)
        else:
            openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            return _get_openai_response(openai_client, prompt, model, temperature, max_tokens)
    elif 'chat_google' in provider.lower():
        if async_llm:
            return await _get_async_chat_google_generativeai_response(prompt, model, temperature, max_tokens)
        else:
            return _get_chat_google_generativeai_response(prompt, model, temperature, max_tokens)
    elif 'google' in provider.lower():
        if async_llm:
            return await _get_async_google_generativeai_response(prompt, model, temperature, max_tokens)
        else:
            return _get_google_generativeai_response(prompt, model, temperature, max_tokens)
    elif 'chat_vertexai' in provider.lower():
        if async_llm:
            return await _get_async_chat_vertexai_response(prompt, model, temperature, max_tokens)
        else:
            return _get_chat_vertexai_response(prompt, model, temperature, max_tokens)
    elif 'vertexai' in provider.lower():
        if async_llm:
            return await _get_async_vertexai_response(prompt, model, temperature, max_tokens)
        else:
            return _get_vertexai_response(prompt, model, temperature, max_tokens)
    elif 'anthropic' in provider.lower():
        if async_llm:
            async_anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            return await _get_async_anthropic_response(async_anthropic_client, prompt, model, temperature, max_tokens)
        else:
            anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            return _get_anthropic_response(anthropic_client, prompt, model, temperature, max_tokens)
    elif 'groq' in provider.lower():
        if async_llm:
            async_groq_client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
            return await _get_async_groq_response(async_groq_client, prompt, model, temperature, max_tokens)
        else:
            groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            return _get_groq_response(groq_client, prompt, model, temperature, max_tokens)
    elif 'litellm' in provider.lower():
        if async_llm:
            return await _get_async_litellm_response(prompt, model, temperature, max_tokens)
        else:
            return _get_litellm_response(prompt, model, temperature, max_tokens)


@trace_llm(name="_get_openai_response")
def _get_openai_response(
    openai_client,
    prompt,
    model, 
    temperature,
    max_tokens,
    ):
    """
    Get response from OpenAI API
    """
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {str(e)}")
        return None

@trace_llm(name="_get_async_openai_response")
async def _get_async_openai_response(
    async_openai_client,
    prompt,
    model, 
    temperature,
    max_tokens,
    ):
    """
    Get async response from OpenAI API
    """
    try:
        response = await async_openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with async OpenAI API: {str(e)}")
        return None

@trace_llm(name="_get_openai_beta_response")
def _get_openai_beta_response(
    openai_client,
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    assistant = openai_client.beta.assistants.create(model=model)
    thread = openai_client.beta.threads.create()
    message = openai_client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = openai_client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        temperature=temperature,
        max_completion_tokens=max_tokens
    )
    if run.status == 'completed':
        messages = openai_client.beta.threads.messages.list(thread_id=thread.id)
        return messages.data[0].content[0].text.value

@trace_llm(name="_get_azure_openai_response")
def _get_azure_openai_response(
    azure_openai_client,
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get response from Azure OpenAI API
    """
    try:
        response = azure_openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with Azure OpenAI API: {str(e)}")
        return None

@trace_llm(name="_get_async_azure_openai_response")
async def _get_async_azure_openai_response(
    async_azure_openai_client,
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get async response from Azure OpenAI API
    """
    try:
        response = await async_azure_openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with async Azure OpenAI API: {str(e)}")
        return None

@trace_llm(name="_get_litellm_response")
def _get_litellm_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get response using LiteLLM
    """
    try:
        response = completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with LiteLLM: {str(e)}")
        return None

@trace_llm(name="_get_async_litellm_response")
async def _get_async_litellm_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get async response using LiteLLM
    """
    try:
        response = await acompletion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with async LiteLLM: {str(e)}")
        return None

@trace_llm(name="_get_vertexai_response")
def _get_vertexai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get response from VertexAI
    """
    try:
        # vertexai.init(project="gen-lang-client-0655603261", location="us-central1")
        model = GenerativeModel(
            model_name=model
            )
        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.text
    except Exception as e:
        print(f"Error with VertexAI: {str(e)}")
        return None

@trace_llm(name="_get_async_vertexai_response")
async def _get_async_vertexai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get async response from VertexAI
    """
    try:
        model = GenerativeModel(
            model_name=model
            )
        response = await model.generate_content_async(
            prompt,
            generation_config=GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.text
    except Exception as e:
        print(f"Error with async VertexAI: {str(e)}")
        return None

@trace_llm(name="_get_google_generativeai_response")
def _get_google_generativeai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get response from Google GenerativeAI
    """
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.text
    except Exception as e:
        print(f"Error with Google GenerativeAI: {str(e)}")
        return None

@trace_llm(name="_get_async_google_generativeai_response")
async def _get_async_google_generativeai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    """
    Get async response from Google GenerativeAI
    """
    try:
        model = genai.GenerativeModel(model)
        response = await model.generate_content_async(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.text
    except Exception as e:
        print(f"Error with async Google GenerativeAI: {str(e)}")
        return None

@trace_llm(name="_get_anthropic_response")
def _get_anthropic_response(
    anthropic_client,
    prompt,
    model, 
    temperature,
    max_tokens,
    ):
    try:
        response = anthropic_client.messages.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error with Anthropic: {str(e)}")
        return None

@trace_llm(name="_get_async_anthropic_response")
async def _get_async_anthropic_response(
    async_anthropic_client,
    prompt,
    model, 
    temperature,
    max_tokens, 
    ):
    try:
        response = await async_anthropic_client.messages.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error with async Anthropic: {str(e)}")
        return None

@trace_llm(name="_get_chat_google_generativeai_response")
def _get_chat_google_generativeai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        model = ChatGoogleGenerativeAI(model=model)
        response = model._generate(
            [HumanMessage(content=prompt)],
            generation_config=dict(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.generations[0].text
    except Exception as e:
        print(f"Error with Google GenerativeAI: {str(e)}")
        return None

@trace_llm(name="_get_async_chat_google_generativeai_response")
async def _get_async_chat_google_generativeai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        model = ChatGoogleGenerativeAI(model=model)
        response = await model._agenerate(
            [HumanMessage(content=prompt)],
            generation_config=dict(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.generations[0].text
    except Exception as e:
        print(f"Error with async Google GenerativeAI: {str(e)}")
        return None

@trace_llm(name="_get_chat_vertexai_response")
def _get_chat_vertexai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        model = ChatVertexAI(
            model=model, 
            google_api_key=os.getenv("GOOGLE_API_KEY")
            )
        response = model._generate(
            [HumanMessage(content=prompt)],
            generation_config=dict(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.generations[0].text
    except Exception as e:
        print(f"Error with VertexAI: {str(e)}")
        return None

@trace_llm(name="_get_async_chat_vertexai_response")
async def _get_async_chat_vertexai_response(
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        model = ChatVertexAI(
            model=model, 
            google_api_key=os.getenv("GOOGLE_API_KEY")
            )
        response = await model._agenerate(
            [HumanMessage(content=prompt)],
            generation_config=dict(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.generations[0].text
    except Exception as e:
        print(f"Error with async VertexAI: {str(e)}")
        return None

@trace_llm(name="_get_groq_response")
def _get_groq_response(
    groq_client,
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        response = groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with Groq: {str(e)}")
        return None

@trace_llm(name="_get_async_groq_response")
async def _get_async_groq_response(
    async_groq_client,
    prompt,
    model, 
    temperature,
    max_tokens
    ):
    try:
        response = await async_groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with async Groq: {str(e)}")
        return None

