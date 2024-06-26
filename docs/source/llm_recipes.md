## LLMs Quantization Recipes

Intel® Neural Compressor supported advanced large language models (LLMs) quantization technologies including SmoothQuant (SQ) and Weight-Only Quant (WOQ),
and verified a list of LLMs on 4th Gen Intel® Xeon® Scalable Processor (codenamed Sapphire Rapids) with [PyTorch](https://pytorch.org/),
[Intel® Extension for PyTorch](https://github.com/intel/intel-extension-for-pytorch) and [Intel® Extension for Transformers](https://github.com/intel/intel-extension-for-transformers).  
This document aims to publish the specific recipes we achieved for the popular LLMs and help users to quickly get an optimized LLM with limited 1% accuracy loss.

> Notes:
>
> - The quantization algorithms provide by [Intel® Neural Compressor](https://github.com/intel/neural-compressor) and the evaluate functions provide by [Intel® Extension for Transformers](https://github.com/intel/intel-extension-for-transformers).
> - The model list are continuing update, please expect to find more LLMs in the future.

## Large Language Models Recipes

|             Models              | SQ INT8 | WOQ INT8 | WOQ INT4 |
| :-----------------------------: | :-----: | :------: | :------: |
|       EleutherAI/gpt-j-6b       |    ✔    |    ✔     |    ✔     |
|        facebook/opt-1.3b        |    ✔    |    ✔     |    ✔     |
|        facebook/opt-30b         |    ✔    |    ✔     |    ✔     |
|    meta-llama/Llama-2-7b-hf     |    ✔    |    ✔     |    ✔     |
|    meta-llama/Llama-2-13b-hf    |    ✔    |    ✔     |    ✔     |
|    meta-llama/Llama-2-70b-hf    |    ✔    |    ✔     |    ✔     |
|        tiiuae/falcon-7b         |    ✔    |    ✔     |    ✔     |
|        tiiuae/falcon-40b        |    ✔    |    ✔     |    ✔     |
| baichuan-inc/Baichuan-13B-Chat  |    ✔    |    ✔     |    ✔     |
| baichuan-inc/Baichuan2-13B-Chat |    ✔    |    ✔     |    ✔     |
| baichuan-inc/Baichuan2-7B-Chat  |    ✔    |    ✔     |    ✔     |
|      bigscience/bloom-1b7       |    ✔    |    ✔     |    ✔     |
|     databricks/dolly-v2-12b     |    ✖    |    ✔     |    ✖     |
|     EleutherAI/gpt-neox-20b     |    ✖    |    ✔     |    ✔     |
|    mistralai/Mistral-7B-v0.1    |    ✖    |    ✔     |    ✔     |
|        THUDM/chatglm2-6b        |    ✔    |    ✔     |    ✔     |
|        THUDM/chatglm3-6b        |   WIP   |    ✔     |   WIP    |

**Detail recipes can be found [HERE](https://github.com/intel/intel-extension-for-transformers/blob/main/examples/huggingface/pytorch/text-generation/quantization/llm_quantization_recipes.md).**

> Notes:
>
> - This model list comes from [IPEX](https://intel.github.io/intel-extension-for-pytorch/cpu/latest/tutorials/llm.html).
> - The WIP recipes will be published soon.

## Large Language Models Accuracy

<table><thead>
  <tr>
    <th rowspan="3">Model</th>
    <th colspan="9">lambada_openai</th>
  </tr>
  <tr>
    <th>FP32</th>
    <th colspan="2">SQ INT8</th>
    <th colspan="2">WOQ INT8</th>
    <th colspan="2">WOQ INT4 GPTQ</th>
    <th colspan="2">WOQ INT4 AutoRound</th>
  </tr>
  <tr>
    <th>ACC</th>
    <th>ACC</th>
    <th>Ratio</th>
    <th>ACC</th>
    <th>Ratio</th>
    <th>ACC</th>
    <th>Ratio</th>
    <th>ACC</th>
    <th>Ratio</th>
  </tr></thead>
<tbody>
  <tr>
    <td>baichuan-inc/Baichuan-13B-Chat</td>
    <td>67.57%</td>
    <td>69.07%</td>
    <td>1.0222</td>
    <td>67.55%</td>
    <td>0.9997</td>
    <td>68.12%</td>
    <td>1.0081</td>
    <td>66.93%</td>
    <td>0.9905</td>
  </tr>
  <tr>
    <td>baichuan-inc/Baichuan2-13B-Chat</td>
    <td>71.51%</td>
    <td>75.57%</td>
    <td>1.0568</td>
    <td>71.57%</td>
    <td>1.0008</td>
    <td>70.81%</td>
    <td>0.9902</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>baichuan-inc/Baichuan2-7B-Chat</td>
    <td>67.67%</td>
    <td>68.06%</td>
    <td>1.0058</td>
    <td>67.61%</td>
    <td>0.9991</td>
    <td>67.90%</td>
    <td>1.0034</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>bigscience/bloom-1b7</td>
    <td>46.34%</td>
    <td>47.99%</td>
    <td>1.0356</td>
    <td>46.21%</td>
    <td>0.9972</td>
    <td>46.90%</td>
    <td>1.0121</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>databricks/dolly-v2-12b</td>
    <td>64.35%</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>63.92%</td>
    <td>0.9933</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>EleutherAI/gpt-j-6b</td>
    <td>68.31%</td>
    <td>68.27%</td>
    <td>0.9994</td>
    <td>68.27%</td>
    <td>0.9994</td>
    <td>68.35%</td>
    <td>1.0006</td>
    <td>68.02%</td>
    <td>0.9958</td>
  </tr>
  <tr>
    <td>EleutherAI/gpt-neox-20b</td>
    <td>72.33%</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>72.29%</td>
    <td>0.9994</td>
    <td>71.74%</td>
    <td>0.9918</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>facebook/opt-1.3b</td>
    <td>57.89%</td>
    <td>57.68%</td>
    <td>0.9964</td>
    <td>58.12%</td>
    <td>1.0040</td>
    <td>58.26%</td>
    <td>1.0064</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>facebook/opt-30b</td>
    <td>71.49%</td>
    <td>71.78%</td>
    <td>1.0041</td>
    <td>71.53%</td>
    <td>1.0006</td>
    <td>71.59%</td>
    <td>1.0014</td>
    <td>71.80%</td>
    <td>1.0043</td>
  </tr>
  <tr>
    <td>meta-llama/Llama-2-13b-hf</td>
    <td>76.77%</td>
    <td>76.25%</td>
    <td>0.9932</td>
    <td>76.89%</td>
    <td>1.0016</td>
    <td>77.66%</td>
    <td>1.0116</td>
    <td>76.60%</td>
    <td>0.9978</td>
  </tr>
  <tr>
    <td>meta-llama/Llama-2-70b-hf</td>
    <td>79.64%</td>
    <td>79.14%</td>
    <td>0.9937</td>
    <td>79.62%</td>
    <td>0.9997</td>
    <td>80.09%</td>
    <td>1.0057</td>
    <td>79.68%</td>
    <td>1.0005</td>
  </tr>
  <tr>
    <td>meta-llama/Llama-2-7b-hf</td>
    <td>73.92%</td>
    <td>73.45%</td>
    <td>0.9936</td>
    <td>73.90%</td>
    <td>0.9997</td>
    <td>73.84%</td>
    <td>0.9989</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>mistralai/Mistral-7B-v0.1</td>
    <td>75.90%</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>75.80%</td>
    <td>0.9987</td>
    <td>76.25%</td>
    <td>1.0046</td>
    <td>75.74%</td>
    <td>0.9979</td>
  </tr>
  <tr>
    <td>THUDM/chatglm2-6b</td>
    <td>53.23%</td>
    <td>52.86%</td>
    <td>0.9930</td>
    <td>53.00%</td>
    <td>0.9957</td>
    <td>52.90%</td>
    <td>0.9938</td>
    <td>52.92%</td>
    <td>0.9942</td>
  </tr>
  <tr>
    <td>THUDM/chatglm3-6b</td>
    <td>59.09%</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>59.03%</td>
    <td>0.9990</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>tiiuae/falcon-40b</td>
    <td>77.22%</td>
    <td>76.95%</td>
    <td>0.9965</td>
    <td>77.18%</td>
    <td>0.9995</td>
    <td>77.55%</td>
    <td>1.0043</td>
    <td>77.82%</td>
    <td>1.0078</td>
  </tr>
  <tr>
    <td>tiiuae/falcon-7b</td>
    <td>74.67%</td>
    <td>76.63%</td>
    <td>1.0262</td>
    <td>74.73%</td>
    <td>1.0008</td>
    <td>75.06%</td>
    <td>1.0052</td>
    <td>74.00%</td>
    <td>0.9910</td>
  </tr>
</tbody></table>
