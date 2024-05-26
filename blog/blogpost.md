# Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning

### Chimène Blokesch, Dominykas Šeputis, Idries Nasim, Job Gräber, Soham Chatterjee

---

## 1. Introduction

Large Language Models (LLMs) have ushered in a new era in natural language understanding, demonstrating exceptional performance across a wide array of tasks. Despite their achievements rooted in identifying statistical patterns and contextual associations, LLMs face notable limitations in performing complex logical reasoning.

One primary limitation is their inability to execute implicit reasoning. Although LLMs excel at capturing surface-level semantics and context, they lack the explicit reasoning mechanisms that humans employ to construct formal proofs or derive conclusions from premises [(Liu et al., 2023b)](https://arxiv.org/abs/2304.03439). Representing intricate logical structures like quantifiers, predicates, and entailments poses a significant challenge. Moreover, the faithfulness of LLMs—including their consistency, coherence, and adherence to logical rules—is often compromised. Consequently, they might produce responses that sound plausible but fall short of true logical validity. This shortcoming is particularly glaring in tasks demanding precise logical inference.

Additionally, LLMs are prone to hallucinations—inaccurately generating information that seems correct but is actually false. The inherent ambiguity of natural language presents further obstacles. LLMs frequently rely on statistical probabilities to resolve ambiguities, which can result in occasional errors or misinterpretations. In logical reasoning, where precise disambiguation is essential, this reliance can be particularly detrimental.

<br/>
<p align="center">
    <img src="https://preview.redd.it/comics-drawing-of-the-week-raising-ai-v0-f221aklb9z7c1.jpg?width=1690&format=pjpg&auto=webp&s=a042adea690d3de93d732ff730edf713cc075767" width=300px>
</p>
<br/>

In response to these constraints, the [Logic-LM](https://github.com/teacherpeterpan/Logic-LLM) framework has been introduced. This innovative approach integrates the capabilities of LLMs with the precision of symbolic solvers. Logic-LM begins by converting natural language problem descriptions into symbolic representations, effectively bridging the gap between human-readable text and the rigorous language of logic. Once a symbolic formulation is established, a deterministic symbolic solver takes over. Unlike LLMs, which rely on statistical heuristics, these solvers strictly adhere to formal rules, manipulate logical expressions, conduct deductive reasoning, and validate hypotheses with high accuracy.

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

### 2.1 Problem formulation

Logic programming is a programming paradigm that is particularly well-suited for tasks involving symbolic reasoning and knowledge representation. It is fundamentally different from imperative programming in that it expresses computation through logical declarations and relationships rather than explicit control flow. In logic programming, problems are formulated as a set of logical statements, often in the form of predicates, which describe facts and rules about problems within a given domain. The most well-known logic programming language is Prolog. In Prolog, computation is driven by the engine's attempt to satisfy queries by systematically searching for and applying rules and facts. The declarative nature of logic programming often leads to more concise, flexible, and understandable code, as it allows programmers to focus on “what” needs to be achieved rather than “how” to achieve it.

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

### 2.2 Symbolic reasoning

The ability to reason is crucial for maximizing the utility of knowledge, particularly in problem-solving, decision-making, and critical thinking. Proficient abstract reasoning enables a model to effectively address unfamiliar problems. As LLMs continue to find diverse and widespread applications, the capacity for reasoning plays a pivotal role in their success. However, it remains uncertain whether transformer-based LLMs inherently possess this generalized ability, thereby creating a strong incentive to explore alternative methods for enhancing it. Symbolic solvers, designed to be sound and efficiently decidable, offer a dependable means of facilitating general reasoning. Nevertheless, symbolic solvers require specific formal input. By integrating the flexibility of LLMs with the soundness and efficiency of symbolic solvers, Logic-LM represents a promising approach to enhancing and further advancing reasoning capabilities.

An important benefit of employing symbolic solvers is their deterministic nature. In contrast to LLMs, which produce outputs using probabilistic models and statistical patterns, symbolic solvers operate according to strict logical rules. This deterministic methodology guarantees that the reasoning process is both accurate and transparent. Accuracy pertains to the solver's capacity to strictly adhere to logical principles without introducing errors or inconsistencies. Transparency, on the other hand, is achieved because each stage of the reasoning process can be traced and validated against logical rules.

Furthermore, Logic-LM incorporates an iterative refinement process. During inference, if the symbolic solver encounters errors or inconsistencies, it generates error messages. These messages are then used by the self-refinement module to iteratively revise the symbolic representation. This iterative process continues until the symbolic formulation accurately captures the intended logical structure of the problem, thereby enhancing both accuracy and coherence.

The incorporation of symbolic solvers into the Logic-LM framework illustrates a hybrid approach that leverages the natural language understanding capabilities of LLMs while embracing the rigor and precision of symbolic reasoning. This integration not only overcomes the inherent limitations of LLMs in logical reasoning but also paves the way for more robust and interpretable language models that can effectively tackle complex reasoning tasks with greater accuracy. The integration of symbolic solvers into the Logic-LM framework exemplifies a hybrid approach that combines the strengths of LLMs in natural language understanding with the rigor and precision of symbolic reasoning. By doing so, Logic-LM not only addresses the inherent limitations of LLMs in logical reasoning but also sets the stage for more robust and interpretable language models capable of tackling complex reasoning tasks with higher fidelity.

### 2.3 Result interpreter

Once the symbolic solver has completed the necessary inferences and generated a solution, the resulting solution is typically presented in a formal, symbolic format. While this format is precise and suitable for logical validation, it may not be easily accessible or interpretable for users who are more familiar with natural language. The Result Interpreter addresses this issue by converting the symbolic answers into natural language responses.

This translation process involves several steps. Firstly, the formal symbolic representations are parsed and analyzed to extract the fundamental logical components and their relationships. Subsequently, these components are matched with their corresponding natural language expressions. The Result Interpreter must ensure that this matching accurately preserves the logical structure and meaning of the original symbolic answer, thereby upholding the accuracy and integrity of the reasoning process.

The incorporation of the Result Interpreter into the Logic-LM framework elevates the interpretability of the system’s outputs. Users can gain access to clear and succinct explanations of intricate logical inferences, which can prove particularly beneficial in applications like automated theorem proving, complex question answering, and semantic parsing. Through the transformation of symbolic solutions into natural language, the Result Interpreter ensures that the logical precision of the symbolic solver remains intact in the interpretation process.
Furthermore, the Result Interpreter plays a significant role in the iterative refinement process. By offering natural language feedback on the results produced by the symbolic solver, it can aid in identifying ambiguities or inconsistencies in the initial problem formulation. This feedback can then be utilized to iteratively refine and enhance the symbolic representation, ultimately leading to more precise and coherent final outputs.

### 2.4 Datasets

We incorporated logical reasoning datasets including ProofWriter (Tafjord et al., 2020), PrOntoQA (Saparov & He, 2022), FOLIO (Han, 2022), AR-LSAT (Han et al., 2022), and LogicalDeduction from BigBench (Srivastava et al., 2022), supplemented by multi-modal data from the SET (Webb, 2023) card game.

### 2.5 LLMs

For our project, we leveraged advanced models such as OpenAI's ChatGPT for natural language processing (NLP) tasks, Google's Gemini for comparisons and analysis, and open-source language models (LLMs) like LLAMA, accessing them through their respective application programming interfaces (APIs).

## 3. Results

Our project focused on investigating the learning capabilities of Logic-LM in various contexts and identifying potential limitations. We conducted extensive studies on different datasets with varying levels of complexity to understand the strengths and weaknesses of the model. In addition, we explored the effectiveness of using symbolic solvers in a multi-modal setting and investigated the potential of integrating differentiable neuro-symbolic solvers to fine-tune training models for generating accurate logic programs.

Our research built upon the work of Pan (2023) by emphasizing in-context learning for logical problem-solving and adapting LLMs to this domain using techniques such as Low-Rank Adaptation (LoRA) (Hu, 2021).

Expanding on Pan’s research, which primarily focused on textual inputs, our project extended the scope to include multi-modal foundation models. We evaluated their effectiveness in solving logical problems using both text and visual inputs. Our experiments involved challenges such as the SET game, where the model interpreted visual input from SET cards and a textual query to identify valid sets. Additionally, we explored similar scenarios using games like Sudoku, Suguru, and various card games, all of which had established solvers and frameworks suitable for generating examples for few-shot learning.

For the ablation Studies, our primary objective was to expand on Pan’s research by conducting comprehensive ablation studies to validate and potentially build upon the authors’ findings.

### 3.1 Multi-modal Logic Reasoning

In a multi-modal setting, the Large Language Model (LLM) is provided not only with textual data but also with other forms of data, such as images. The LLM must extract crucial information from these diverse data types to perform reasoning tasks effectively.

#### 3.1.1 Datasets for Multi-modal Logic Reasoning

The multi-modal logic reasoning experiments were conducted using synthetic datasets specifically created for tasks like Sudoku and Graph Coloring problems. These datasets included various types of data representations such as graphs, Sudoku puzzles, and the SET card games. In addition to these data structures, a textual prompt was also provided to specify the task at hand and the desired output format.

|    Dataset name     |                                                             Model's task                                                             | Logic representation & solver |                 Example input image                 |
| :-----------------: | :----------------------------------------------------------------------------------------------------------------------------------: | :---------------------------: | :-------------------------------------------------: |
|  **Graph Fill-in**  |                      Filling in the missing color in a graph so that no two adjacent nodes have the same color.                      |         ASP & Clingo          |  <img src="./media/graph_fill_in.png" width="300">  |
| **Graph Validity**  | Determining whether it is possible to color a graph with a given set of colors such that no two adjacent nodes have the same color.  |         ASP & Clingo          | <img src="./media/graph_validity.png" width="300">  |
| **Sudoku Fill-in**  |                                          Filling in the missing numbers in a Sudoku puzzle.                                          |         ASP & Clingo          | <img src="./media/sudoku_fill_in.png" width="300">  |
| **Sudoku Validity** |                                         Determining whether a given Sudoku puzzle is valid.                                          |         ASP & Clingo          | <img src="./media/sudoku_validity.png" width="300"> |
|       **SET**       | Following the card game rules, find the sets given the cards shown in the image. The same cards can appear and are counted as a set. |         ASP & Clingo          |       <img src="./media/SET.png" width="300">       |

Validity datasets contained 400 samples (except for SET validity, which included 200 samples), with 200 valid and 200 invalid examples each. For fill-in problems, 200 samples were created. Validity problems had two possible answers (Yes or No), while fill-in problems had four different options (for Sudoku, these were the possible missing numbers; for graph coloring, they were the missing colors). For multiple choice problems, we employed Answer Set Programming (ASP) programs to ensure there was only one correct answer by validating model counts.

The datasets were created by combining both textual and visual inputs. The textual inputs were generated by converting logical problems into natural language descriptions, while the visual inputs were crafted to visualize these logical problems. Models were prompted with both the textual and visual inputs to solve the problems, employing a one-example in-context learning strategy in all cases.

For direct prompting, models were provided with a sample question, an accompanying picture, and the correct answer. For ASP prompting, models received a sample question, an accompanying picture, an ASP program representing the problem, and the correct answer.

#### 3.1.2 ASP as a Symbolic Language

We utilized an additional symbolic language, Answer Set Programming (ASP), to represent the multi-modal logic problems. ASP is more restricted than First-Order Logic (FOL) but is simpler to program. ASP programs can be solved using tools like Clingo.

Below is an example program used for the Graph Fill-in dataset:

```prolog
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

#### 3.1.3 Results for Multi-modal Logic Reasoning

We evaluated the multi-modal LLM from the Gemini family (`gemini-1.5-pro-preview-0409`) using both ASP and direct prompting strategies. To validate the ASP-generated code, we employed the Clingo solver. The results are summarized below:

<table>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax" colspan="6">Accuracy % for prompting type</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">Dataset<br></td>
    <td class="tg-baqh">Direct <br><span style="font-weight:bold"><b>Gemini Pro</b></span></td>
    <td class="tg-baqh">Direct<br><span style="font-weight:bold"><b>Gemini Flash</b></span></td>
    <td class="tg-baqh">Direct<br><span style="font-weight:bold"><b>GPT-4</b></span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold"><b>Gemini Pro</b></span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold"><b>Gemini Flash</b></span></td>
    <td class="tg-baqh">ASP<br><span style="font-weight:bold"><b>GPT-4</b></span></td>
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

As we can see from the results, the model achieves much higher accuracy when prompted with ASP programs compared to direct prompting. This indicates that the model is able to better understand the logical problems when provided with ASP programs, which are more structured and explicit compared to direct prompts.

While analyzing the mistakes made by the model using direct prompting, we observed that the model often struggled to correctly understand the logical problems, leading to incorrect answers and increased hallucinations. Performance for all models usually did not exceed random guessing.

The SET validity task appeared to be the most challenging for the models, with the lowest accuracy across all datasets. This could be due to the complexity of the task, which involves identifying valid sets based on both visual and textual inputs.

For ASP prompting, the primary mistakes made by the model were related to generating the problem representation as a valid ASP program. Since the provided ASP programs required precise encoding of either Sudoku boards or graph coloring problems, the model often failed to generate correct ASP programs. This was especially evident in the Graph Fill-in problem, where the model struggled to encode the graph coloring problem accurately. Interestingly, the problems for fill-in tasks were mostly not caused by incorrect world representation, but by failing to correctly define the missing number or color. This occurred even when, while encoding the state, models correctly omitted the missing number or color.

```prolog
% Defining the initial Sudoku grid
sudoku(1,1,3). sudoku(1,2,8). sudoku(1,3,1). sudoku(1,4,4). sudoku(1,5,2). sudoku(1,6,9). sudoku(1,7,6). sudoku(1,8,5). sudoku(1,9,7). sudoku(2,1,4). sudoku(2,2,6). sudoku(2,3,7). sudoku(2,4,3). sudoku(2,5,5). sudoku(2,6,8). sudoku(2,7,2). sudoku(2,8,9). sudoku(2,9,1). sudoku(3,1,2). sudoku(3,2,5). sudoku(3,3,9). sudoku(3,4,7). sudoku(3,5,6). sudoku(3,6,1). sudoku(3,7,8). sudoku(3,8,3). sudoku(3,9,4). sudoku(4,1,1). sudoku(4,2,7). sudoku(4,3,8). sudoku(4,4,6). sudoku(4,5,3). sudoku(4,6,5). sudoku(4,7,9). sudoku(4,8,4). sudoku(4,9,2). sudoku(5,1,6). sudoku(5,2,9). sudoku(5,3,4). sudoku(5,4,2). sudoku(5,5,1). sudoku(5,6,7). sudoku(5,7,5). sudoku(5,8,8). sudoku(5,9,3). sudoku(6,1,5). sudoku(6,2,3). sudoku(6,3,2). sudoku(6,4,8). sudoku(6,5,9). sudoku(6,6,4). sudoku(6,8,1). sudoku(6,9,6). sudoku(7,1,8). sudoku(7,2,2). sudoku(7,3,5). sudoku(7,4,1). sudoku(7,5,4). sudoku(7,6,6). sudoku(7,7,3). sudoku(7,8,7). sudoku(7,9,9). sudoku(8,1,7). sudoku(8,2,1). sudoku(8,3,6). sudoku(8,4,9). sudoku(8,5,8). sudoku(8,6,3). sudoku(8,7,4). sudoku(8,8,2). sudoku(8,9,5). sudoku(9,1,9). sudoku(9,2,4). sudoku(9,3,3). sudoku(9,4,5). sudoku(9,5,7). sudoku(9,6,2). sudoku(9,7,1). sudoku(9,8,6). sudoku(9,9,8).

% OUR COMMENT
% While model correctly did not include the missing number in the state (sudoku(6,7,N)), it failed to correctly define the missing number in the answer.

% Find the missing number in cell (7,6)
1 { sudoku(7,6,N) : n(N) } 1.
```

Interestingly, [while GPT-4 performs better or similarly in most benchmarks](https://openai.com/index/hello-gpt-4o/), it significantly underperforms in multi-modal reasoning tasks. Although it achieves competitive performance in direct prompting, it struggles to encode the ASP programs correctly, leading to a substantial drop in accuracy. Most issues stem from hallucinating nodes or edges that are not present in the graph or failing to correctly define the missing number or color.

#### Note on Cost and Performance

We used Microsoft Azure to run the GPT-4 model and Google Vertex AI to run the Gemini models. The cost to run all multi-modal experiments for GPT-4 was 82 euros, while for Gemini models, the cost for running two models was 40 euros. More interestingly, the average time per inference for GPT-4 was 66 seconds, whereas for Gemini Pro it was 21 seconds and for Gemini Flash 8 seconds. Considering both cost and performance, Gemini Flash emerges as the best choice for multi-modal reasoning.

| Model        | Cost (Euros) | Average Inference Time | Cost and Performance Evaluation   |
| ------------ | ------------ | ---------------------- | --------------------------------- |
| GPT-4        | 82           | 66 seconds             | High cost, slower performance     |
| Gemini Pro   | 40           | 21 seconds             | Moderate cost, faster performance |
| Gemini Flash | 40           | 8 seconds              | Best value, fastest performance   |

### 3.2 Prompting - Ablation Experiments - In Context Learning

We evaluated the LLama family of models, i.e. `meta-llama/Llama-2-7b-chat-hf` and `meta-llama/Meta-Llama-3-8B-Instruct`. In general, LLama3 performs way better than LLama2. The results table below are conducted wrt Llama3. We found that for logical tasks, where we have to predict one option out of 5 available options, the model is somewhat biased towards predicting the first choice. Additionally, if we allow generating more tokens by increasing the max_new_tokens hyperparameter, i.e. increasing the maximum number of tokens to generate, the quality of the logic programs gets better. Additionally, we also performed an experiment when we prompted the model to predict all the incorrect options. We get higher accuracy in this case, since we have 4 incorrect choices and 1 correct choice per sample. So, predicting a wrong answer is easier compared to the correct one.

|                        Dataset                         | Prompting | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :----------------------------------------------------: | :-------: | :----------------------------------------------------: |
|                    AR-LSAT Baseline                    |  Direct   |                         19.56                          |
| AR-LSAT Swap the correct answer always to first choice |  Direct   |                           25                           |
|          AR-LSAT Predict wrong answer choices          |  Direct   |                           26                           |

Additionally, below table demonstrates the Direct, CoT and Logic-LM results on all datasets with Llama3(meta-llama/Meta-Llama-3-8B-Instruct):

|     Dataset      |                             Prompting                             | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :--------------: | :---------------------------------------------------------------: | :----------------------------------------------------: |
|     ProntoQA     |                   Direct ( 16 max_new_tokens )                    |                           43                           |
|     ProntoQA     |                    CoT ( 1024 max_new_tokens )                    |                          76.6                          |
|     ProntoQA     |                Logic-LM (random backup strategy )                 |                           55                           |
|     ProntoQA     | Logic-LM (Direct-Logic collaboration mode (LLM) backup strategy ) |                         42.46                          |
|     ProntoQA     |  Logic-LM (CoT-Logic collaboration mode (LLM) backup strategy )   |                           8                            |
|   ProofWriter    |                   Direct ( 16 max_new_tokens )                    |                           33                           |
|   ProofWriter    |                    CoT ( 1024 max_new_tokens )                    |                         28.54                          |
|   ProofWriter    |                Logic-LM (random backup strategy )                 |                          28.7                          |
|   ProofWriter    | Logic-LM (Direct-Logic collaboration mode (LLM) backup strategy ) |                         28.69                          |
|   ProofWriter    |  Logic-LM (CoT-Logic collaboration mode (LLM) backup strategy )   |                         28.695                         |
|      FOLIO       |                   Direct ( 16 max_new_tokens )                    |                          46.5                          |
|      FOLIO       |                    CoT ( 1024 max_new_tokens )                    |                           36                           |
|      FOLIO       |                Logic-LM (random backup strategy )                 |                           43                           |
|      FOLIO       | Logic-LM (Direct-Logic collaboration mode (LLM) backup strategy ) |                           53                           |
|      FOLIO       |  Logic-LM (CoT-Logic collaboration mode (LLM) backup strategy )   |                         44.285                         |
| LogicalDeduction |                   Direct ( 16 max_new_tokens )                    |                         32.33                          |
| LogicalDeduction |                    CoT ( 1024 max_new_tokens )                    |                           22                           |
| LogicalDeduction |                Logic-LM (random backup strategy )                 |                         24.27                          |
| LogicalDeduction | Logic-LM (Direct-Logic collaboration mode (LLM) backup strategy ) |                           31                           |
| LogicalDeduction |  Logic-LM (CoT-Logic collaboration mode (LLM) backup strategy )   |                         20.38                          |
|     AR-LSAT      |                   Direct ( 16 max_new_tokens )                    |                          7.36                          |
|     AR-LSAT      |                    CoT ( 1024 max_new_tokens )                    |                         8.225                          |
|     AR-LSAT      |                Logic-LM (random backup strategy )                 |                           22                           |
|     AR-LSAT      | Logic-LM (Direct-Logic collaboration mode (LLM) backup strategy ) |                           12                           |
|     AR-LSAT      |  Logic-LM (CoT-Logic collaboration mode (LLM) backup strategy )   |                           6                            |

### 3.3 Gemini results

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

From these tables it is clear that there is not one dominant model, since between the five tasks there are three different models performing best. Furthermore, models that perform best on a certain task, may completely fail to generate executable logic programs on another task. On inspection, such total failure is due to the model being unable to follow the instructions concerning the formatting of the logic program. So it will for example add explanations for what it is doing in natural language in places where it will break the logic program. There does not seem to be a clear pattern in when a model fails in this way. Even models that are presumably similar like gemini-1.5-pro-preview-0409 and gemini-1.5-pro-preview-0514 give unpredictably different results in this regard. Recall here that we sample with 0 temperature. This points to an important fragility in the Logic-LM approach. Besides random total failures, there is the case of AR-LSAT where no model performs well. Analysis of the mistakes suggests that the model does not understand parts of the syntax of the z3 solver. It will try to use functionalities from the z3 solver incorrectly. This is probably due to there not being enough z3 code in the pre-training data and the few shot examples not covering certain aspects of the language. Exploratory experimentation with ~750k prompts simply also containing all documentation for z3 did not solve the problems.

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

## 4. Concluding Remarks

In this blogpost, we discussed Logic-LM, a novel framework that seamlessly integrates Large Language Models (LLMs) with symbolic solvers to enhance logical reasoning capabilities. By converting natural language problems into structured symbolic representations and employing deterministic solvers, Logic-LM achieves precise and consistent logical reasoning. We extended the research by replicating the results with other models and investigated multi-modal reasoning. The multi-modal experiments demonstrate its ability to handle both textual and visual inputs, while ablation studies provide insights into prompting strategies. Despite challenges and fragility, Logic-LM represents a promising approach for robust and interpretable language models in complex reasoning tasks.

## 5. Student Contributions

Dominykas Šeputis and Chimène Blokesch focused primarily on multi-modal foundation models to assess their ability to address logical issues using both textual and visual inputs. Soham Chatterjee delved into how LLMs behave to different prompting approaches, such as Direct, Chain of Thought, Few shot including more prompt examples, investigated the effectiveness by forcing LLMs to output incorrect choices and performed extensive ablation studies with 5 different datasets, each corresponding to a logical task with Direct, Chain of Thought and Logic-LM approaches. Job Gräber led the adaptation of LLMs for logic problem-solving through fine-tuning methods. Idries Nasim primarily oversaw the coordination of experiments and the drafting of the research report, also providing assistance with ablation studies as needed. All team members made active contributions by presenting the results of their experiments.

## 6. Bibliography

Liu, H., Ning, R., Teng, Z., Liu, J., Zhou, Q., & Zhang, Y. (2023). Evaluating the logical reasoning ability of chatgpt and gpt-4. arXiv preprint arXiv:2304.03439.

Han, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell,
M., et al. Folio: Natural language reasoning with first-order logic. arXiv preprint arXiv:2209.00840 (2022).

Webb, T., Holyoak, K. J., and Lu, H. Emergent analogical reasoning in large language models. Nature Human
Behaviour 7, 9 (2023), 1526–1541.

Tafjord, O., Mishra, B. D., and Clark, P. Proofwriter: Generating implications, proofs, and abductive statements
over natural language. arXiv preprint arXiv:2012.13048 (2020).

Saparov, A., and He, H. Language models are greedy reasoners: A systematic formal analysis of chain-of-thought. arXiv
preprint arXiv:2210.01240 (2022).

Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta,
A., Garriga-Alonso, A., et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language
models. arXiv preprint arXiv:2206.04615 (2022).

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35, 24824-24837.
