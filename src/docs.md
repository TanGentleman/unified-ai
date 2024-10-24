# YAML
"""
model_list:
  - model_name: string
    litellm_params: {}
    model_info:
      id: string
      mode: embedding
      input_cost_per_token: 0
      output_cost_per_token: 0
      max_tokens: 2048
      base_model: gpt-4-1106-preview
      additionalProp1: {}
"""
"""
model_list:
  - model_name: lmstudio-Llama-1B
    litellm_params:
      model: openai/llama-3.2-1b-instruct
      api_key: "os.environ/LMSTUDIO_API_KEY"
      api_base: http://host.docker.internal:1234/v1
  - model_name: Qwen2.5-72B
    litellm_params:
      model: openai/Qwen/Qwen2.5-72B-Instruct-Turbo
      api_base: https://api.together.xyz/v1
      api_key: "os.environ/TOGETHER_API_KEY"
  - model_name: gpt-4o
    litellm_params:
      model: openai/gpt-4o
      api_key: "os.environ/OPENAI_API_KEY"
  - model_name: claude-3.5-sonnet
    litellm_params:
      model: openai/anthropic/claude-3.5-sonnet:beta
      api_key: "os.environ/OPENROUTER_API_KEY"
      api_base: https://openrouter.ai/api/v1
  - model_name: Llama-3.1-405B
    litellm_params:
      model: openai/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo
      api_base: https://api.together.xyz/v1
      api_key: "os.environ/TOGETHER_API_KEY"
"""

# Typescript
"""
export interface Model {
  id: string;
  updated_at: string;
  created_at: string;
  name: string;
  prompt: string;
  option: string;
  temperature: string;
  pinned: boolean;
  vision?: boolean;
  base_url?: string;
}
"""
"""
import { LocalStorage, showToast, Toast } from "@raycast/api";
import { useCallback, useEffect, useMemo, useState, useRef } from "react";
import { Model, ModelHook } from "../type";
import { getConfiguration, useChatGPT } from "./useChatGPT";
import { useProxy } from "./useProxy";

export const DEFAULT_MODEL: Model = {
  id: "default",
  updated_at: new Date().toISOString(),
  created_at: new Date().toISOString(),
  name: "Default",
  prompt: "You are a helpful assistant.",
  option: "gpt-4o-mini",
  temperature: "1",
  pinned: false,
  vision: false,
};

export function useModel(): ModelHook {...}
"""