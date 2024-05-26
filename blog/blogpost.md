# LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning

### Chimène Blokesch, Dominykas Šeputis, Idries Nasim, Job Gräber, Soham Chatterjee

---

## 1. Introduction

Large Language Models (LLMs) have ushered in a new era in natural language understanding, demonstrating exceptional performance across a wide array of tasks. Despite their achievements rooted in identifying statistical patterns and contextual associations, LLMs face notable limitations in performing complex logical reasoning.

One primary limitation is their inability to execute implicit reasoning. Although LLMs excel at capturing surface-level semantics and context, they lack the explicit reasoning mechanisms that humans employ to construct formal proofs or derive conclusions from premises [(Liu et al., 2023b)](link). Representing intricate logical structures like quantifiers, predicates, and entailments poses a significant challenge. Moreover, the faithfulness of LLMs—including their consistency, coherence, and adherence to logical rules—is often compromised. Consequently, they might produce responses that sound plausible but fall short of true logical validity. This shortcoming is particularly glaring in tasks demanding precise logical inference.

Additionally, LLMs are prone to hallucinations—inaccurately generating information that seems correct but is actually false. The inherent ambiguity of natural language presents further obstacles. LLMs frequently rely on statistical probabilities to resolve ambiguities, which can result in occasional errors or misinterpretations. In logical reasoning, where precise disambiguation is essential, this reliance can be particularly detrimental.

<br/>
<p align="center">
    <img src="https://preview.redd.it/comics-drawing-of-the-week-raising-ai-v0-f221aklb9z7c1.jpg?width=1690&format=pjpg&auto=webp&s=a042adea690d3de93d732ff730edf713cc075767" width=300px>
</p>
<br/>

In response to these constraints, the [Logic-LM](https://arxiv.org/pdf/2305.12295) framework has been introduced. This innovative approach integrates the capabilities of LLMs with the precision of symbolic solvers. Logic-LM begins by converting natural language problem descriptions into symbolic representations, effectively bridging the gap between human-readable text and the rigorous language of logic. Once a symbolic formulation is established, a deterministic symbolic solver takes over. Unlike LLMs, which rely on statistical heuristics, these solvers strictly adhere to formal rules, manipulate logical expressions, conduct deductive reasoning, and validate hypotheses with high accuracy.

Inspired by the proposed solution of enhancing LLMs' logical problem-solving capabilities by integrating symbolic solvers into the workflow, this blog aims to replicate and expand upon the results presented in ["Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"](https://arxiv.org/pdf/2305.12295). The objectives of this blog are as follows:

1. Clarify Logic-LM's framework and methodology.
2. Replicate the results from the paper, expanding on the ablation studies.
3. Explore the capabilities of different LLM families within the context of Logic-LM.
4. Investigate the multi-modal reasoning capabilities of Logic-LM.

## 2. Logic-LM Framework

The Logic-LM framework's reasoning process comprises three main stages: Problem Formulation, Symbolic Reasoning, and Result Interpretation.

**Problem Formulation:** In this stage, the Large Language Model (LLM) converts the problem from natural language into a symbolic format. This involves identifying essential entities, facts, and rules within the problem statement, effectively translating human-readable text into a structured logical representation.

**Symbolic Reasoning:** During this stage, a deterministic symbolic solver is employed to perform inference based on the symbolic formulation created in the previous stage. Unlike LLMs, which rely on statistical heuristics, the symbolic solver strictly adheres to formal rules, thereby ensuring precise and consistent logical reasoning.

**Result Interpretation:** In the final stage, an interpreter is used to explain the output of the symbolic solver, aligning it with the correct answer and making it comprehensible to the user.

This structured approach allows the Logic-LM framework to effectively address complex reasoning tasks. Compared to the direct prompting approach, **Logic Programming (LP) prompting** enables the model to generate more accurate and coherent logical reasoning outputs by following a systematic thought framework. This approach is similar to the [chain-of-thought prompting](https://arxiv.org/abs/2201.11903), but it is based on symbolic reasoning rather than purely statistical methods.

<br/>
<p align="center">
  <img src="./media/workflow.png" width=600px>
</p>
<br/>

### 2.1 Logic programming

Logic programming is a programming paradigm that is particularly well-suited for tasks involving symbolic reasoning and knowledge representation. It is fundamentally different from imperative programming in that it expresses computation through logical declarations and relationships rather than explicit control flow. In logic programming, problems are formulated as a set of logical statements, often in the form of predicates, which describe facts and rules about problems within a given domain. The most well-known logic programming language is Prolog. In Prolog, computation is driven by the engine's attempt to satisfy queries by systematically searching for and applying rules and facts. The declarative nature of logic programming often leads to more concise, flexible, and understandable code, as it allows programmers to focus on "what" needs to be achieved rather than "how" to achieve it.

For example, below you can see a simple program that seeks to find which of the given birds can fly:

```prolog
% First, we define the facts about the birds, where object is a type of bird and each bird has a name.
penguin(tweety).
parrot(polly).
sparrow(sid).
broken_wing(sid).
ostrich(olga).

% Next, we define the rules that determine whether a previously defined object is a bird.
bird(X) :- penguin(X).
bird(X) :- parrot(X).
bird(X) :- sparrow(X).
bird(X) :- ostrich(X).

% Finally, we define the rules that determine whether a bird can fly.
cannot_fly(X) :- penguin(X).
cannot_fly(X) :- ostrich(X).
cannot_fly(X) :- broken_wing(X).

% A bird can fly if it is a bird and it cannot fly.
can_fly(X) :- bird(X), not cannot_fly(X).

% Query to find birds that can fly.
#hide.
#show can_fly(X).
```

There is a great blog, that introduces basic of answer set programming, which is a subset of logic programming, and how to use it to solve problems. You can find it [here](https://ddmler.github.io/asp/2018/07/06/answer-set-programming-the-basics.html).

### 2.1 symbolic reasoning


The ability to reason is crucial for maximizing the utility of knowledge, particularly in problem-solving, decision-making, and critical thinking. Proficient abstract reasoning enables a model to effectively address unfamiliar problems. As LLMs continue to find diverse and widespread applications, the capacity for reasoning plays a pivotal role in their success. However, it remains uncertain whether transformer-based LLMs inherently possess this generalized ability, thereby creating a strong incentive to explore alternative methods for enhancing it. Symbolic solvers, designed to be sound and efficiently decidable, offer a dependable means of facilitating general reasoning. Nevertheless, symbolic solvers require specific formal input. By integrating the flexibility of LLMs with the soundness and efficiency of symbolic solvers, Logic-LM represents a promising approach to enhancing and further advancing reasoning capabilities.

An important benefit of employing symbolic solvers is their deterministic nature. In contrast to LLMs, which produce outputs using probabilistic models and statistical patterns, symbolic solvers operate according to strict logical rules. This deterministic methodology guarantees that the reasoning process is both accurate and transparent. Accuracy pertains to the solver's capacity to strictly adhere to logical principles without introducing errors or inconsistencies. Transparency, on the other hand, is achieved because each stage of the reasoning process can be traced and validated against logical rules.

Furthermore, LOGIC-LM incorporates an iterative refinement process. During inference, if the symbolic solver encounters errors or inconsistencies, it generates error messages. These messages are then used by the self-refinement module to iteratively revise the symbolic representation. This iterative process continues until the symbolic formulation accurately captures the intended logical structure of the problem, thereby enhancing both accuracy and coherence.

The incorporation of symbolic solvers into the LOGIC-LM framework illustrates a hybrid approach that leverages the natural language understanding capabilities of LLMs while embracing the rigor and precision of symbolic reasoning. This integration not only overcomes the inherent limitations of LLMs in logical reasoning but also paves the way for more robust and interpretable language models that can effectively tackle complex reasoning tasks with greater accuracy. The integration of symbolic solvers into the LOGIC-LM framework exemplifies a hybrid approach that combines the strengths of LLMs in natural language understanding with the rigor and precision of symbolic reasoning. By doing so, LOGIC-LM not only addresses the inherent limitations of LLMs in logical reasoning but also sets the stage for more robust and interpretable language models capable of tackling complex reasoning tasks with higher fidelity.

### 2.2 Result interpreter

Once the symbolic solver has completed the necessary inferences and generated a solution, the resulting solution is typically presented in a formal, symbolic format. While this format is precise and suitable for logical validation, it may not be easily accessible or interpretable for users who are more familiar with natural language. The Result Interpreter addresses this issue by converting the symbolic answers into natural language responses.

This translation process involves several steps. Firstly, the formal symbolic representations are parsed and analyzed to extract the fundamental logical components and their relationships. Subsequently, these components are matched with their corresponding natural language expressions. The Result Interpreter must ensure that this matching accurately preserves the logical structure and meaning of the original symbolic answer, thereby upholding the accuracy and integrity of the reasoning process.

The incorporation of the Result Interpreter into the LOGIC-LM framework elevates the interpretability of the system’s outputs. Users can gain access to clear and succinct explanations of intricate logical inferences, which can prove particularly beneficial in applications like automated theorem proving, complex question answering, and semantic parsing. Through the transformation of symbolic solutions into natural language, the Result Interpreter ensures that the logical precision of the symbolic solver remains intact in the interpretation process.
Furthermore, the Result Interpreter plays a significant role in the iterative refinement process. By offering natural language feedback on the results produced by the symbolic solver, it can aid in identifying ambiguities or inconsistencies in the initial problem formulation. This feedback can then be utilized to iteratively refine and enhance the symbolic representation, ultimately leading to more precise and coherent final outputs.

### 2.3 Datasets

We will incorporate logical reasoning datasets including ProofWriter (arXiv:2012.13048), PrOntoQA (arXiv:2210.01240), FOLIO (Han, 2022), AR-LSAT (arXiv:2209.00840), and LogicalDeduction from BigBench (arXiv:2206.04615), supplemented by multi-modal data from the SET (Webb, 2023). Additionally, we aim to enhance our models' reasoning capabilities with a differentiable solver, such as Diff-SAT.

## 3. Reproduction of the Experiments

## 4. Novel Contribution

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

For our project, we intend to leverage advanced models such as OpenAI's ChatGPT for natural language processing (NLP) tasks, Google's Gemini for comparisons and analysis, and open-source language models (LLMs) like LLAMA, accessing them through their respective application programming interfaces (APIs). Both the ChatGPT and Gemini APIs are subscription-based, with estimated costs in the tens of euros, subject to change based on request volumes and additional services.

### Multi-modal Logic Reasoning

In a multi-modal setting, not only textual data is given to the LLM, but also other structures of data, such as images, can be utilized as input. The LLM needs to extract the important information from the input data to be able to reason about it.

### Datasets Multi-modal

The multi-modal logic reasoning experiments were conducted by building synthetic datasets for Sudoku and Graph Coloring problems. Different datasets were created based on graphs, sudoku's and the SET card games. A textual prompt is also given to specify the task and the desired output format.

|    Dataset name     |                                                             Model's task                                                             | Logic representation & solver |                 Example input image                 |
| :-----------------: | :----------------------------------------------------------------------------------------------------------------------------------: | :---------------------------: | :-------------------------------------------------: |
|  **Graph Fill-in**  |                      Filling in the missing color in a graph so that no two adjacent nodes have the same color.                      |         ASP & Clingo          |  <img src="./media/graph_fill_in.png" width="300">  |
| **Graph Validity**  | Determining whether it is possible to color a graph with a given set of colors such that no two adjacent nodes have the same color.  |         ASP & Clingo          | <img src="./media/graph_validity.png" width="300">  |
| **Sudoku Fill-in**  |                                          Filling in the missing numbers in a Sudoku puzzle.                                          |         ASP & Clingo          | <img src="./media/sudoku_fill_in.png" width="300">  |
| **Sudoku Validity** |                                         Determining whether a given Sudoku puzzle is valid.                                          |         ASP & Clingo          | <img src="./media/sudoku_validity.png" width="300"> |
|       **SET**       | Following the card game rules, find the sets given the cards shown in the image. The same cards can appear and are counted as a set. |         ASP & Clingo          |       <img src="./media/SET.png" width="300">       |

Validity datasets contained 400 samples, with 200 valid and 200 invalid examples each. For fill-in problems, 200 samples were created. Validity problems had two possible answers (Yes, No) and Fill-in problems had four different options (for Sudoku, possible missing numbers; for graph, missing colors). For multiple choice problems, we employed ASP programs to ensure that there is only one correct answer by validating models count.

The datasets were created by combining textual and visual inputs. The textual inputs were generated by converting the logical problems into natural language descriptions, while the visual inputs were created by visualizing the logical problems. Models were prompted with both the textual and visual inputs to solve the problems, employing a one-example in-context learning strategy in all cases.

For direct prompting, models were given a sample question, an accompanying picture, and the correct answer. For ASP prompting, models were given a sample question, an accompanying picture, an ASP program that represents the problem, and the correct answer.

### ASP as symbolic language

We utilized an additional symbolic language to represent the multi-modal logic problems, namely Answer Set Programming (ASP). This language is more restricted than First-Order Logic (FOL), but is simpler to program. Its programs can be solved using Clingo. Below, an example program is given, which is used for the Graph Fill-in dataset.

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

### Results Multi-modal

We evaluated the multi-modal LLM from the Gemini family `gemini-1.5-pro-preview-0409` using both ASP and direct prompting strategies. To validate the ASP-generated code, we employed the Clingo solver. The results are summarized below:

<table>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax" colspan="6">Accuracy % for prompting type</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">Dataset<br></td>
    <td class="tg-baqh">Direct <br><span style="font-weight:bold">Gemini Pro</span></td>
    <td class="tg-baqh">Direct<br><span style="font-weight:bold">Gemini Flash</span></td>
    <td class="tg-baqh">Direct<br><span style="font-weight:bold">GPT-4</span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold">Gemini Pro</span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold">Gemini Flash</span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold">GPT-4</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">Sudoku Fill-in</td>
    <td class="tg-0lax">28.50</td>
    <td class="tg-0lax">25.51</td>
    <td class="tg-0lax">23.50</td>
    <td class="tg-0lax"><b>67.50</b></td>
    <td class="tg-0lax">22.00</td>
    <td class="tg-0lax">29.64</td>
  </tr>
  <tr>
    <td class="tg-0lax">Sudoku Validity</td>
    <td class="tg-0lax">47.25</td>
    <td class="tg-0lax">48.03</td>
    <td class="tg-0lax">49.50</td>
    <td class="tg-0lax">92.08</td>
    <td class="tg-0lax"><b>93.00</b></td>
    <td class="tg-0lax">87.75</td>
  </tr>
  <tr>
    <td class="tg-0lax">Graph Fill-in</td>
    <td class="tg-0lax">36.65</td>
    <td class="tg-0lax">29.50</td>
    <td class="tg-0lax">26.00</td>
    <td class="tg-0lax"><b>65.01</b></td>
    <td class="tg-0lax">38.21</td>
    <td class="tg-0lax">28.01</td>
  </tr>
  <tr>
    <td class="tg-0lax">Graph Validity</td>
    <td class="tg-0lax">54.75</td>
    <td class="tg-0lax">54.00</td>
    <td class="tg-0lax">52.51</td>
    <td class="tg-0lax"><b>94.50<b/></td>
    <td class="tg-0lax">90.50</td>
    <td class="tg-0lax">86.25</td>
  </tr>
  <tr>
    <td class="tg-0lax">SET Validity</td>
    <td class="tg-0lax">58.00</td>
    <td class="tg-0lax">55.51</td>
    <td class="tg-0lax">53.01</td>
    <td class="tg-0lax"><b>67.00</b></td>
    <td class="tg-0lax">48.51</td>
    <td class="tg-0lax">54.51</td>
  </tr>
</tbody></table>

As we can see from the results, the model achieves much higher accuracy when prompted with ASP programs compared to direct prompting. This indicates that the model is able to better understand the logical problems when provided with the ASP programs, which are more structured and explicit compared to direct prompts.

While analyzing the mistakes made by the model using direct prompting, we observed that the model often struggled to correctly understand the logical problems, leading to incorrect answers and increased hallucinations.

For the ASP prompting, the primary mistakes made by the model were related to generating the problem representation as a valid ASP program. As the provided ASP programs required precise encoding of either Sudoku boards or graph coloring problems, the model often failed to generate correct ASP programs. This was especially evident in the Graph Fill-in problem, where the model struggled to correctly encode the graph coloring problem.

### Prompting - Ablation Experiments - In Context Learning

We evaluated the LLama family of models,ie- `meta-llama/Llama-2-7b-chat-hf` and `meta-llama/Meta-Llama-3-8B-Instruct`. In general, LLama3 performs way better than LLama2. The results table below are conducted wrt Llama3. We found that for logical tasks, where we have to predict one option out of 5 available options, the model is somewhat biased towards predicting the first choice. Additionally, if we allow to generate more tokens by increaisng the max_new_tokens hyper-parmater,ie- increasing the maximum number of tokens to generate, the quality of the logic programs gets better. Additionally, we also performed an experiment when we prompted the model to predict all the incorrect options. We get higher accuracy in this case since we have 4 incorrect choices and 1 correct choice per sample. So, predicing a wrong answer is easier compared to the correct one.

|                        Dataset                         | Prompting | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :----------------------------------------------------: | :-------: | :----------------------------------------------------: |
|                    AR-LSAT Baseline                    |  Direct   |                         19.56                          |
| AR-LSAT Swap the correct answer always to first choice |  Direct   |                           25                           |
|          AR-LSAT Predict wrong answer choices          |  Direct   |                           26                           |

Additionally, below table demonstrates the Direct, CoT and Logic-LM results on all datasets with Llama3(meta-llama/Meta-Llama-3-8B-Instruct):

|     Dataset      |                            Prompting                             | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :--------------: | :--------------------------------------------------------------: | :----------------------------------------------------: |
|     ProntoQA     |                   Direct ( 16 max_new_tokens )                   |                           43                           |
|     ProntoQA     |                   CoT ( 1024 max_new_tokens )                    |                          76.6                          |
|     ProntoQA     |                Logic-LM (random backup strategy )                |                           55                           |
|     ProntoQA     | Logic-LM (Direct-Logic collabration mode (LLM) backup strategy ) |                         42.46                          |
|     ProntoQA     |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |                           8                            |
|   ProofWriter    |                   Direct ( 16 max_new_tokens )                   |                           33                           |
|   ProofWriter    |                   CoT ( 1024 max_new_tokens )                    |                         28.54                          |
|   ProofWriter    |                Logic-LM (random backup strategy )                |                          28.7                          |
|   ProofWriter    | Logic-LM (Direct-Logic collabration mode (LLM) backup strategy ) |                         28.69                          |
|   ProofWriter    |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |                         28.695                         |
|      FOLIO       |                   Direct ( 16 max_new_tokens )                   |                          46.5                          |
|      FOLIO       |                   CoT ( 1024 max_new_tokens )                    |                           36                           |
|      FOLIO       |                Logic-LM (random backup strategy )                |                           43                           |
|      FOLIO       | Logic-LM (Direct-Logic collabration mode (LLM) backup strategy ) |                           53                           |
|      FOLIO       |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |                         44.285                         |
| LogicalDeduction |                   Direct ( 16 max_new_tokens )                   |                         32.33                          |
| LogicalDeduction |                   CoT ( 1024 max_new_tokens )                    |                           22                           |
| LogicalDeduction |                Logic-LM (random backup strategy )                |                         24.27                          |
| LogicalDeduction | Logic-LM (Direct-Logic collabration mode (LLM) backup strategy ) |                           31                           |
| LogicalDeduction |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |                         20.38                          |
|     AR-LSAT      |                   Direct ( 16 max_new_tokens )                   |                          7.36                          |
|     AR-LSAT      |                   CoT ( 1024 max_new_tokens )                    |                         8.225                          |
|     AR-LSAT      |                Logic-LM (random backup strategy )                |                           22                           |
|     AR-LSAT      | Logic-LM (Direct-Logic collabration mode (LLM) backup strategy ) |                           12                           |
|     AR-LSAT      |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |                           6                            |

### Gemini results

Evaluation logic programs per task with backup option 'CoT'. Best results per row in bold.

| ProntoQA            | gemini-1.0-pro-vision-001 | gemini-1.5-pro-preview-0409 | gemini-1.5-pro-preview-0514 | gemini-1.5-flash-preview-0514 |
| ------------------- | ------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Overall_Accuracy    | 92.60                     | **97.40**                   | 93.00                       | 92.60                         |
| Executable_Rate     | 0.00                      | **96.40**                   | 0.00                        | 0.00                          |
| Executable_Accuracy | 0.00                      | **97.30**                   | 0.00                        | 0.00                          |

| ProofWriter         | gemini-1.0-pro-vision-001 | gemini-1.5-pro-preview-0409 | gemini-1.5-pro-preview-0514 | gemini-1.5-flash-preview-0514 |
| ------------------- | ------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Overall_Accuracy    | 74.12                     | **78.04**                   | 66.17                       | 66.17                         |
| Executable_Rate     | 64.44                     | **89.36**                   | 0.00                        | 4.67                          |
| Executable_Accuracy | 76.17                     | **80.53**                   | 0.00                        | 53.57                         |

| FOLIO               | gemini-1.0-pro-vision-001 | gemini-1.5-pro-preview-0409 | gemini-1.5-pro-preview-0514 | gemini-1.5-flash-preview-0514 |
| ------------------- | ------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Overall_Accuracy    | 63.50                     | 75.25                       | **80.60**                   | 59.80                         |
| Executable_Rate     | 48.50                     | 58.42                       | **78.11**                   | 4.41                          |
| Executable_Accuracy | 68.04                     | 83.05                       | 85.35                       | **100.00**                    |

| LogicalDeduction    | gemini-1.0-pro-vision-001 | gemini-1.5-pro-preview-0409 | gemini-1.5-pro-preview-0514 | gemini-1.5-flash-preview-0514 |
| ------------------- | ------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Overall_Accuracy    | 64.67                     | 64.67                       | **84.67**                   | 57.67                         |
| Executable_Rate     | 60.00                     | 60.00                       | **100.00**                  | 71.67                         |
| Executable_Accuracy | **89.44**                 | 87.22                       | 84.67                       | 69.77                         |

| AR-LSAT             | gemini-1.0-pro-vision-001 | gemini-1.5-pro-preview-0409 | gemini-1.5-pro-preview-0514 | gemini-1.5-flash-preview-0514 |
| ------------------- | ------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Overall_Accuracy    | 24.35                     | 23.81                       | 34.20                       | **35.50**                     |
| Executable_Rate     | 0.00                      | 0.00                        | 26.41                       | **33.77**                     |
| Executable_Accuracy | 0.00                      | 0.00                        | **60.66**                   | 60.26                         |

From these tables it is clear that there is not one dominant model since between the five tasks there are three different models performing best. Furthermore, models that perform best on a certain task, may completely fail to generate executable logic programs on another task. On inspection such total failure is due to the model being unable to follow the instructions concerning the formatting of the logic program. So it will for example add explanations for what it is doing in natural language in places where it will break the logic program. There does not seem to be a clear pattern in when a model fails in this way. Even models that are presumably similar like gemini-1.5-pro-preview-0409 and gemini-1.5-pro-preview-0514 give unpredicatbly different results in this regard. Recall here that we sample with 0 temperature. This points to an important fragility in the Logic-LM approach. Besides random total failures, there is the case of AR-LSAT where no model performs well. Analysis of the mistakes suggests that the model does not understand parts of the syntax of the z3 solver. It will try to use functionalities from the z3 solver in an incorrect way. This is probably due to there not being enought z3 code in the pre-training data and the few shot examples not covering certain aspects of the language. Exploratory experimention with ~750k prompts simply also containing all documentation for z3 did not solve the problems.

Evaluation of the baselines with Gemini. All baselines results (Direct and CoT) are done with gemini-1.5-flash-preview-0514. Best accuracy score of the Logic-LM approach with the CoT backup strategy is presented for comparison.

| dataset          | mode     | accuracy  | best model                    |
| ---------------- | -------- | --------- | ----------------------------- |
| ProntoQA         | Direct   | 63.80     | -                             |
| -                | CoT      | 92.34     | -                             |
| -                | Logic-LM | **97.40** | gemini-1.5-pro-preview-0409   |
| ProofWriter      | Direct   | 53.83     | -                             |
| -                | CoT      | 65.15     | -                             |
| -                | Logic-LM | **78.04** | gemini-1.5-pro-preview-0409   |
| FOLIO            | Direct   | 66.67     | -                             |
| -                | CoT      | 49.25     | -                             |
| -                | Logic-LM | **80.60** | gemini-1.5-pro-preview-0514   |
| LogicalDeduction | Direct   | 54.67     | -                             |
| -                | CoT      | 30.00     | -                             |
| -                | Logic-LM | **84.67** | gemini-1.5-pro-preview-0514   |
| AR-LSAT          | Direct   | 27.95     | -                             |
| -                | CoT      | 20.35     | -                             |
| -                | Logic-LM | **35.50** | gemini-1.5-flash-preview-0514 |

Here we see that the results of the Logic-LM approach with the best model significantly outperforms both direct and CoT prompting. Note however that the fragility noted above means that it is not necessarily clear a priori which model would be the best for the Logic-LM approach.

## 5. Concluding Remarks

TODO

## Student Contributions

Dominykas Šeputis and Chimène Blokesch focused primarily on multi-modal foundation models to assess their ability to address logical issues using both textual and visual inputs. Soham Chatterjee delved into how LLMs behave to different prompting approaches, such as Direct, Chain of Thought, Few shot inluding more prompt examples, investigated the effectiveness by forcing LLMs to output incorrect choices and performed extensive ablation studies with 5 different datasets, each corresponding to a logical task with Direct, Chain of Thought and Logic-LM approaches. Job Gräber led the adaptation of LLMs for logic problem-solving through fine-tuning methods. Idries Nasim primarily oversaw the coordination of experiments and the drafting of the research report, also providing assistance with ablation studies as needed. All team members made active contributions by presenting the results of their experiments.

## Bibliography

HanmengLiu, Ruoxi Ning, Zhiyang Teng, Jian Liu, Qiji
Zhou, and Yue Zhang. 2023b. Evaluating the logi
cal reasoning ability of chatgpt and GPT-4. CoRR,
abs/2304.03439

Han, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell,
M., et al. Folio: Natural language reasoning with first-order logic. arXiv preprint arXiv:2209.00840 (2022).

Webb, T., Holyoak, K. J., and Lu, H. Emergent analogical reasoning in large language models. Nature Human
Behaviour 7, 9 (2023), 1526–1541.
