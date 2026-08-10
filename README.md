# Inference Endpoint Templates

A collection of templates for building and deploying LLM inference endpoints. Each template is a self-contained example you can adapt for your own serving needs.

## What's inside

| Directory | Description |
| --- | --- |
| `custom-endpoint/` | Minimal FastAPI + Hugging Face endpoint exposing a `/generate` text-generation API. |
| `openai-endpoint/` | FastAPI + Hugging Face endpoint with an OpenAI-style interface and RAG over web content. |
| `chatcrc-endpoint/` | Conversational RAG chat endpoint (FastAPI + LangChain + LangGraph) with a retrieval engine. |
| `triton-multimodel-endpoint/` | NVIDIA Triton Inference Server setup for serving multiple Hugging Face transformer models. |
| `llm-service/` | Kubernetes deployment manifests (deployments, services, secrets, volumes) for an LLM API service on Minikube. |
| `minikube-recipes/` | Minikube YAML recipes and chat templates for vLLM-based LLM deployments. |
