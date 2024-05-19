# LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning

### Chimène Blokesch, Dominykas Šeputis, Idries Nasim, Job Gräber, Soham Chatterjee

---

## Introduction

The article introduces LOGIC-LM, an innovative framework created to augment Large Language Models (LLMs) with symbolic solvers to improve logical reasoning. This approach integrates natural language comprehension of LLMs with deterministic symbolic solvers to address logical problems. The framework consists of three main stages: Problem Formulation, Symbolic Reasoning, and Result Interpretation, with a self-refinement module for continuously enhancing symbolic formulations based on feedback from the solver's error messages. This integration has resulted in a notable performance improvement across different logical reasoning datasets, highlighting the capability of LOGIC-LM in tackling intricate logical reasoning challenges.

While current LLMs can exhibit human-like reasoning, they may still lack fidelity and completeness. In response, Logic-LM (Pan, 2023) leverages symbolic languages to address logical problems, offering a more reliable and interpretable alternative to LLMs. However, the in-context learning proposed by Pan (2023) does not consistently yield executable or accurate programs. Our objective is to replicate, enhance, and expand upon these findings. This will involve conducting ablation studies with varying numbers of in-context examples, different LLMs, and different solvers, as well as incorporating negative examples. Additionally, we will explore fine-tuning using differentiable neuro-symbolic solvers, enabling backpropagation from the reasoning task. Furthermore, we will investigate whether the fundamental concept of Logic-LM applies to multi-modal input.

In contrast to previous approaches, prior works have concentrated on enhancing the reasoning capabilities of LLMs through fine-tuning, in-context learning, or information extraction from external sources. Although Logic-LM outperforms LLMs in solving logic problems, it depends on translating reasoning problems into logical formats that can be addressed by symbolic solvers.

Consequently, the model's applicability is inherently constrained by the expressiveness of the symbolic solver. For instance, not all problems can be easily encoded in first-order logic. Furthermore, it relies on in-context learning combined with self-refinement to convert a natural language problem into a symbolic representation. Therefore, ambiguity in natural language can result in an incorrect translation to the symbolic solver language, leading to an inaccurate answer. While this approach has been effective, it may encounter challenges when dealing with logical representations with complex grammar structures, such as probabilistic soft logic. This difficulty stems from the limited capacity to convey intricate grammatical rules to the language model within a constrained context size. A valid symbolic representation does not necessarily imply a "correct" problem formulation that accurately represents the issue. Our objective is to address some of these limitations of Logic-LM.
We intend to improve the in-context learning capabilities of the model so that its heavy reliance on symbolic solvers can be reduced as much as possible. Additionally, we want to explore if the model improves its logical reasoning capabilities with multiple modalities, i.e.- if we fine-tune the model with both text and image versions of the logical problem, can it perform better? On a high level, the overall goal is to improve the reasoning capability of LLMs with minimum or possibly zero dependency on external symbolic solvers.

LLMs demonstrate strong performance on certain reasoning benchmarks, yet it remains uncertain whether they possess a general capacity for reasoning or simply excel by relying on memorized patterns and heuristics (Jie Huang, 2023). Previous research has concentrated on enhancing the reasoning abilities of LLMs, which can be achieved through fine-tuning or in-context learning. In the latter, step-by-step explanations are prompted to facilitate understanding of the reasoning process. One example of this approach is chain-of-thought prompting. Another strategy to enhance reasoning performance is the utilization of Tool-augmented Language Models, which have access to external resources for information extraction, such as calculators and information retrievers. Additionally, Auto-Formalization, as employed by Logic-LM, involves translating natural language (NL) into a symbolic language for reasoning, with the subsequent answer being provided in NL through LLM-generated sentences. However, the challenge remains the ambiguity of NL, which can lead to misunderstandings and incorrect reasoning in these methods.
 The paper situates itself within the broader context of research on LLMs and logical reasoning. It builds upon previous works that have adapted LLMs for logical reasoning tasks, such as chain-of-thought prompting and fine-tuning approaches. However, LOGIC-LM distinguishes itself by using symbolic language as the reasoning unit, transferring the burden of executing complex reasoning from LLMs to symbolic solvers. This shift allows for more reliable and interpretable reasoning processes. The paper also contributes to the field of neuro-symbolic methods, proposing a generalizable framework that does not require specialized module designs or extensive training, thus broadening the applicability of LLMs in logical reasoning tasks.

The ability to reason is crucial for maximizing the utility of knowledge, particularly in problem-solving, decision-making, and critical thinking. Proficient abstract reasoning enables a model to effectively address unfamiliar problems. As LLMs continue to find diverse and widespread applications, the capacity for reasoning plays a pivotal role in their success. However, it remains uncertain whether transformer-based LLMs inherently possess this generalized ability, thereby creating a strong incentive to explore alternative methods for enhancing it. Symbolic solvers, designed to be sound and efficiently decidable, offer a dependable means of facilitating general reasoning. Nevertheless, symbolic solvers require specific formal input. By integrating the flexibility of LLMs with the soundness and efficiency of symbolic solvers, Logic-LM represents a promising approach to enhancing and further advancing reasoning capabilities.

---

## Analysis of Weaknesses/Strengths/Potential

It's important to note that LLMs struggle with solving complex logical problems, often leading to unfaithful reasoning and unreliable conclusions. Additionally, their probabilistic nature lacks a mechanism to ensure the faithfulness of reasoning, making it challenging to trust their outputs for critical applications.

LLMs have demonstrated a remarkable capacity to reason like humans when given step-by-step explanations or prompts. Additionally, they show exceptional proficiency in converting natural language problems into symbolic formulations, indicating their potential to complement symbolic solvers.

The ability to reason is crucial for effectively utilizing knowledge, particularly in problem-solving, decision-making, and critical thinking. The capacity to reason abstractly enables a model to effectively tackle unfamiliar problems. As Language Models (LLMs) continue to be applied in various contexts, their success is heavily reliant on this factor. However, it is uncertain whether transformer-based LLMs possess this generalized ability, thus creating a clear incentive to explore alternative methods for enhancing it. Symbolic solvers, designed to be sound and efficiently solvable, offer a promising avenue for promoting generalized reasoning. Nonetheless, symbolic solvers require specific formal input. Logic-LM combines the flexibility of LLMs with the soundness and efficiency of symbolic solvers, representing a promising approach that warrants further development and refinement.

The concept involves enhancing the reasoning capabilities of LLMs by integrating external modules, specifically symbolic solvers. LLMs are responsible for translating natural language problems into a set of rules, facts, variables, and constraints that conform to the symbolic solver's grammar. The logical reasoning process, leading to a conclusion, is managed by the solver. Subsequently, the solver's output is reconverted into natural language. This enhancement will render LLMs valuable in addressing critical problem-solving scenarios.

## Novel Contribution

Our objective is to investigate the in-context learning capabilities of Logic-LM and pinpoint potential scenarios where the model may fall short. We will conduct ablation studies on diverse datasets featuring varying levels of complexity to comprehensively grasp the model's strengths and weaknesses. Additionally, we aim to determine the efficacy of employing symbolic solvers in a multi-modal setting. Lastly, we will explore the potential of integrating differentiable neuro-symbolic solvers to enable fine-tuning for training models to generate accurate logic programs.
Our project bridges two research domains: it builds upon the research of (Pan, 2023) by delving into the potential of in-context learning for logical problem-solving, and it applies model adaptation techniques such as Low-Rank Adaptation (LoRA) (Hu, 2021) to tailor LLMs to this domain. Although our main emphasis is on the former, the latter presents an opportunity for extending our work.

Building upon the research conducted by Pan in 2023, which primarily concentrates on textual inputs, our project seeks to broaden the scope to encompass multi-modal foundation models. Our goal is to assess their effectiveness in solving logical problems utilizing both text and visual inputs. Our experimentation will involve tackling challenges such as the SET game, where the model will be tasked with interpreting the visual input of SET cards alongside a textual query to identify valid sets. Additionally, we will explore similar scenarios using games like Sudoku, Suguru, and various card games, all of which feature established solvers and representational frameworks that are well-suited for generating the necessary examples for few-shot learning.

Ablation Studies: Our main objective is to build upon the research of (Pan, 2023) by conducting comprehensive ablation studies to validate and potentially broaden the authors' discoveries. Our studies will primarily center on in-context learning, with a specific focus on the following:

1. Determining the optimal number (\(k\)) of examples required for the model to achieve optimal results. This will ascertain the efficiency and scalability of in-context learning in real-world scenarios.

2. Assessing the performance of different families of LLMs in a multi-modal setting. We aim to employ models from the Gemini (arXiv:2312.11805) and Llama (arXiv:2302.13971) families to compare their effectiveness against the traditional GPT model family.

3. Exploring the integration of various logical solvers into the learning process, such as Clingo — a solver of Answer Set Programming (ASP), to comprehend the impact of structured logical reasoning on the effectiveness of LLMs.

In addition, we intend to explore alternative in-context learning strategies. While (Pan, 2023) utilizes prompt templates to direct models in delivering accurate answers and justifying their validity, we are considering a different approach. Our proposal involves training the model to recognize all incorrect answers to a logic problem and articulate the reasons for their invalidity. This method is designed to enrich the model's reasoning abilities by fostering a deeper comprehension of logical fallacies.

Refining LLMs: Following the achievement of our initial objectives, our subsequent aim is to refine LLMs to confirm their effectiveness in solving logic problems. We intend to utilize an open-source LLM from the Llama family and implement efficient adaptation methods such as LoRA. The performance of the refined model will be compared with in-context learning models to evaluate their relative effectiveness. There are two approaches to this refinement process. The first involves training the model on additional text data comprising informal problems, followed by a logic program designed to guide the solver to the correct answer. The availability of high-quality data for more complex problems may be limited using this method. The second approach entails refining the model by directly training it on the supervised reasoning task. A challenge is that classical symbolic solvers are not differentiable, making it impossible to use backpropagation-based optimizers to adjust the parameters of LLMs in this manner. However, some neuro-symbolic models function as symbolic solvers while being differentiable, such as diff-SAT. By employing such a neuro-symbolic solver, the LLM can receive a learning signal while being trained directly on the objective task.

Our upcoming focus is on refining LLMs to improve their capacity for solving logic problems using an open-sourced Llama-family LLM and adaptation methods such as LoRA. We will evaluate the effectiveness by comparing the performance of fine-tuned models with in-context learning models. Fine-tuning can be approached in two ways:

1. Direct training on informal problem texts along with logical programs, which may present a challenge due to the limited availability of high-quality, complex problem data.

2. Fine-tuning through supervised reasoning tasks. Traditional symbolic solvers lack differentiability, which hinders backpropagation-based parameter adjustment. We intend to leverage neuro-symbolic models like Diff-SAT, which are both symbolic and differentiable, enabling direct training on reasoning tasks.

For our project, we intend to leverage advanced models such as OpenAI's ChatGPT for natural language processing (NLP) tasks, Google's Gemini for comparisons and analysis, and open-source language models (LLMs) like LLAMA, accessing them through their respective application programming interfaces (APIs). Both the ChatGPT and Gemini APIs are subscription-based, with estimated costs in the tens of euros, subject to change based on request volumes and additional services.

We will incorporate logical reasoning datasets including ProofWriter (arXiv:2012.13048), PrOntoQA (arXiv:2210.01240), FOLIO (Han, 2022), AR-LSAT (arXiv:2209.00840), and LogicalDeduction from BigBench (arXiv:2206.04615), supplemented by multi-modal data from the SET (Webb, 2023). Additionally, we aim to enhance our models' reasoning capabilities with a differentiable solver, such as Diff-SAT.

## Reproduction of the Experiments

## Multimodal Logic Reasoning

The multimodal logic reasoning experiments were conducted by building synthetic datasets for Sudoku and Graph Coloring problems. Four different datasets were created in total: Graph Fill-in, Graph Validity, Sudoku Fill-in, and Sudoku Validity. These datasets are as follows:

- **Graph Fill-in**: The model is tasked with filling in the missing color in a graph so that no two adjacent nodes have the same color.
- **Graph Validity**: The model is tasked with determining whether it is possible to color a graph with a given set of colors such that no two adjacent nodes have the same color.
- **Sudoku Fill-in**: The model is tasked with filling in the missing numbers in a Sudoku puzzle.
- **Sudoku Validity**: The model is tasked with determining whether a given Sudoku puzzle is valid.

Validity datasets contained 400 samples, with 200 valid and 200 invalid examples each. For fill-in problems, 200 samples were created. Validity problems had two possible answers (Yes, No) and Fill-in problems had four different options (for Sudoku, possible missing numbers; for graph, missing colors).

|  Sudoku Fill-in Problem Sample  |  Sudoku Validity Problem Sample  |
| :-----------------------------: | :------------------------------: |
| ![](./media/sudoku_fill_in.png) | ![](./media/sudoku_validity.png) |

|  Graph Fill-in Problem Sample  |  Graph Validity Problem Sample  |
| :----------------------------: | :-----------------------------: |
| ![](./media/graph_fill_in.png) | ![](./media/graph_validity.png) |

The datasets were created by combining textual and visual inputs. The textual inputs were generated by converting the logical problems into natural language descriptions, while the visual inputs were created by visualizing the logical problems. Models were prompted with both the textual and visual inputs to solve the problems, employing a one-example in-context learning strategy in all cases.

For direct prompting, models were given a sample question, an accompanying picture, and the correct answer. For ASP prompting, models were given a sample question, an accompanying picture, an ASP program that represents the problem, and the correct answer.

```
% Example for Graph Coloring Fill-in problem

% Allocate exactly one color to each node
% This rule ensures that each node is assigned exactly one color
1{coloring(Node, Color): color(Color)}1 :- node(Node).

% Constraint to prevent two connected nodes (i.e., nodes connected by an edge) from having the same color
% This ensures that any valid coloring does not assign the same color to adjacent nodes
:- edge(Node1, Node2), coloring(Node1, Color), coloring(Node2, Color).

% Define predefined colorings for specific nodes
color(green).
color(yellow).
color(blue).
color(red).

% Define the nodes and edges in the graph
node(0). node(1). node(2). node(3). node(4). node(5).
edge(0, 4). edge(0, 5). edge(0, 2). edge(1, 2). edge(1, 4). edge(1, 3). edge(2, 3). edge(2, 4).
edge(2, 5). edge(3, 5). edge(3, 4).
% Defining colored node facts
coloring(0,blue).
coloring(1,yellow).
coloring(2,red).
coloring(3,blue).
coloring(4,green).

% Ensure the grey node (node 5)is assigned exactly one color
1 { coloring(5,Color) : color(Color) } 1.
% Define the answer as the color of the grey node
answer(Color) :- coloring(5,Color).

% Output the final answer
#show answer/1.
```

### Results

We evaluated the multimodal LLM from the Gemini family `gemini-1.5-pro-preview-0409` using both ASP and direct prompting strategies. To validate the ASP-generated code, we employed the Clingo solver. The results are summarized below:

|     Dataset     | Prompting | Accuracy |
| :-------------: | :-------: | :------: |
| Sudoku Fill-in  |  Direct   |   0.75   |
| Sudoku Validity |  Direct   |   0.75   |
|  Graph Fill-in  |  Direct   |   0.75   |
| Graph Validity  |  Direct   |   0.75   |
| Sudoku Validity |    ASP    |   0.75   |
| Sudoku Fill-in  |    ASP    |  0.530   |
|  Graph Fill-in  |    ASP    |  0.538   |
| Graph Validity  |    ASP    |   0.75   |

As we can see from the results, the model achieves much higher accuracy when prompted with ASP programs compared to direct prompting. This indicates that the model is able to better understand the logical problems when provided with the ASP programs, which are more structured and explicit compared to direct prompts.

While analyzing the mistakes made by the model using direct prompting, we observed that the model often struggled to correctly understand the logical problems, leading to incorrect answers and increased hallucinations.

For the ASP prompting, the primary mistakes made by the model were related to generating the problem representation as a valid ASP program. As the provided ASP programs required precise encoding of either Sudoku boards or graph coloring problems, the model often failed to generate correct ASP programs. This was especially evident in the Graph Fill-in problem, where the model struggled to correctly encode the graph coloring problem.

## Prompting - Ablation Experiments - In Context Learning ##

We evaluated the LLama family of models,ie- `meta-llama/Llama-2-7b-chat-hf` and `meta-llama/Meta-Llama-3-8B-Instruct`. In general, LLama3 performs way better than LLama2. The results table below are conducted wrt Llama3. We found that for logical tasks, where we have to predict one option out of 5 available options, the model is somewhat biased towards predicting the first choice. Additionally, if we allow to generate more tokens by increaisng the max_new_tokens hyper-parmater,ie- increasing  the maximum number of tokens to generate, the quality of the logic programs gets better.

|     Dataset     | Prompting | Accuracy |
| :-------------: | :-------: | :------: |
| AR-LSAT Baseline  |  Direct   |   19.56   |
| AR-LSAT Swap the correct answer always to first choice |  Direct   |  25   |

Additionally, below table demonstrates the Direct, CoT and Logic-LM results on all datasets with Llama3(meta-llama/Meta-Llama-3-8B-Instruct):

|     Dataset     | Prompting | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct) |
| :-------------: | :-------: | :------: |
| ProntoQA   |  Direct   |      |
| ProntoQA  |  CoT   |     |
| ProntoQA  |  Logic-LM   |     |
| ProofWriter   |  Direct   |      |
| ProofWriter  |  CoT   |     |
| ProofWriter  |  Logic-LM   |     |
| FOLIO   |  Direct   |      |
| FOLIO  |  CoT   |     |
| FOLIO  |  Logic-LM    |     |
| LogicalDeduction   |  Direct   |      |
| LogicalDeduction  |  CoT   |     |
| LogicalDeduction  |  Logic-LM   |     |
| AR-LSAT   |  Direct   |      |
| AR-LSAT  |  CoT   |     |
| AR-LSAT  |  Logic-LM   |     |






## Concluding Remarks

TODO

## Student Contributions

Dominykas Šeputis and Chimène Blokesch focused primarily on multi-modal foundation models to assess their ability to address logical issues using both textual and visual inputs. Soham Chatterjee delved into ablation studies and investigated the effectiveness of the negative Answers in context Learning strategy. Job Gräber led the adaptation of LLMs for logic problem-solving through fine-tuning methods. Idries Nasim primarily oversaw the coordination of experiments and the drafting of the research report, also providing assistance with ablation studies as needed. All team members made active contributions by presenting the results of their experiments.

## Bibliography
