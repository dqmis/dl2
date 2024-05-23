# LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning

### Chimène Blokesch, Dominykas Šeputis, Idries Nasim, Job Gräber, Soham Chatterjee

---
## Introduction

Large Language Models (LLMs) have brought about a new era in natural language understanding, showcasing remarkable capabilities across a wide range of tasks. However, while their success is mainly based on identifying statistical patterns and contextual associations, they are limited in their ability to perform complex logical reasoning.

One significant limitation is the lack of implicit reasoning in LLMs. While they are adept at capturing surface-level semantics and context, they do not possess the explicit reasoning mechanisms used by humans to construct formal proofs or derive conclusions from premises. Representing complex logical structures, such as quantifiers, predicates, and entailments, poses a significant challenge. Furthermore, the faithfulness of LLMs, including their consistency, coherence, and adherence to logical rules, is often compromised. As a result, they may produce responses that sound plausible but lack true logical validity. This deficiency is particularly evident in tasks that require precise logical inference. Additionally, the inherent ambiguity of natural language presents further challenges. LLMs often rely on statistical probabilities to resolve ambiguities, which can lead to occasional errors or misinterpretations. In logical reasoning, where precise disambiguation is crucial, this dependence can be detrimental.

In response to these constraints, the LOGIC-LM framework has been introduced. This novel approach integrates the capabilities of Language Model Models (LLMs) with the accuracy of symbolic solvers. LOGIC-LM commences by converting natural language problem descriptions into symbolic representations, effectively bridging the divergence between human-readable text and the rigorous language of logic. Once a symbolic formulation is established, a deterministic symbolic solver assumes control. In contrast to LLMs, which depend on statistical heuristics, these solvers strictly adhere to formal rules, manipulating logical expressions, conducting deductive reasoning, and validating hypotheses with precision.

Consequently, the model's applicability is inherently constrained by the expressiveness of the symbolic solver. For instance, not all problems can be easily encoded in first-order logic. Furthermore, it relies on in-context learning combined with self-refinement to convert a natural language problem into a symbolic representation. Therefore, ambiguity in natural language can result in an incorrect translation to the symbolic solver language, leading to an inaccurate answer. While this approach has been effective, it may encounter challenges when dealing with logical representations with complex grammar structures, such as probabilistic soft logic. This difficulty stems from the limited capacity to convey intricate grammatical rules to the language model within a constrained context size. A valid symbolic representation does not necessarily imply a "correct" problem formulation that accurately represents the issue. Our objective is to address some of these limitations of Logic-LM.
We intend to improve the in-context learning capabilities of the model so that its heavy reliance on symbolic solvers can be reduced as much as possible. On a high level, the overall goal is to improve the reasoning capability of LLMs with minimum or possibly zero dependency on external symbolic solvers.

---

## symbolic reasoning

While current LLMs can exhibit human-like reasoning, they may still lack fidelity and completeness. In response, Logic-LM (Pan, 2023) leverages symbolic languages to address logical problems, offering a more reliable and interpretable alternative to LLMs. However, the in-context learning proposed by Pan (2023) does not consistently yield executable or accurate programs. Our objective is to replicate, enhance, and expand upon these findings. This will involve conducting ablation studies with varying numbers of in-context examples, different LLMs, and different solvers, as well as incorporating negative examples. Furthermore, we will investigate whether the fundamental concept of Logic-LM applies to multi-modal input.

LLMs demonstrate strong performance on certain reasoning benchmarks, yet it remains uncertain whether they possess a general capacity for reasoning or simply excel by relying on memorized patterns and heuristics (Jie Huang, 2023). Previous research has concentrated on enhancing the reasoning abilities of LLMs, which can be achieved through fine-tuning or in-context learning. In the latter, step-by-step explanations are prompted to facilitate understanding of the reasoning process. One example of this approach is chain-of-thought prompting. Another strategy to enhance reasoning performance is the utilization of Tool-augmented Language Models, which have access to external resources for information extraction, such as calculators and information retrievers. Additionally, Auto-Formalization, as employed by Logic-LM, involves translating natural language (NL) into a symbolic language for reasoning, with the subsequent answer being provided in NL through LLM-generated sentences. However, the challenge remains the ambiguity of NL, which can lead to misunderstandings and incorrect reasoning in these methods.
 The paper situates itself within the broader context of research on LLMs and logical reasoning. It builds upon previous works that have adapted LLMs for logical reasoning tasks, such as chain-of-thought prompting. However, LOGIC-LM distinguishes itself by using symbolic language as the reasoning unit, transferring the burden of executing complex reasoning from LLMs to symbolic solvers. This shift allows for more reliable and interpretable reasoning processes. The paper also contributes to the field of neuro-symbolic methods, proposing a generalizable framework that does not require specialized module designs or extensive training, thus broadening the applicability of LLMs in logical reasoning tasks.

The ability to reason is crucial for maximizing the utility of knowledge, particularly in problem-solving, decision-making, and critical thinking. Proficient abstract reasoning enables a model to effectively address unfamiliar problems. As LLMs continue to find diverse and widespread applications, the capacity for reasoning plays a pivotal role in their success. However, it remains uncertain whether transformer-based LLMs inherently possess this generalized ability, thereby creating a strong incentive to explore alternative methods for enhancing it. Symbolic solvers, designed to be sound and efficiently decidable, offer a dependable means of facilitating general reasoning. Nevertheless, symbolic solvers require specific formal input. By integrating the flexibility of LLMs with the soundness and efficiency of symbolic solvers, Logic-LM represents a promising approach to enhancing and further advancing reasoning capabilities.

An important benefit of employing symbolic solvers is their deterministic nature. In contrast to LLMs, which produce outputs using probabilistic models and statistical patterns, symbolic solvers operate according to strict logical rules. This deterministic methodology guarantees that the reasoning process is both accurate and transparent. Accuracy pertains to the solver's capacity to strictly adhere to logical principles without introducing errors or inconsistencies. Transparency, on the other hand, is achieved because each stage of the reasoning process can be traced and validated against logical rules.

Furthermore, LOGIC-LM incorporates an iterative refinement process. During inference, if the symbolic solver encounters errors or inconsistencies, it generates error messages. These messages are then used by the self-refinement module to iteratively revise the symbolic representation. This iterative process continues until the symbolic formulation accurately captures the intended logical structure of the problem, thereby enhancing both accuracy and coherence.

The incorporation of symbolic solvers into the LOGIC-LM framework illustrates a hybrid approach that leverages the natural language understanding capabilities of LLMs while embracing the rigor and precision of symbolic reasoning. This integration not only overcomes the inherent limitations of LLMs in logical reasoning but also paves the way for more robust and interpretable language models that can effectively tackle complex reasoning tasks with greater accuracy. The integration of symbolic solvers into the LOGIC-LM framework exemplifies a hybrid approach that combines the strengths of LLMs in natural language understanding with the rigor and precision of symbolic reasoning. By doing so, LOGIC-LM not only addresses the inherent limitations of LLMs in logical reasoning but also sets the stage for more robust and interpretable language models capable of tackling complex reasoning tasks with higher fidelity.

## result interpreter

Once the symbolic solver has completed the necessary inferences and generated a solution, the resulting solution is typically presented in a formal, symbolic format. While this format is precise and suitable for logical validation, it may not be easily accessible or interpretable for users who are more familiar with natural language. The Result Interpreter addresses this issue by converting the symbolic answers into natural language responses.

This translation process involves several steps. Firstly, the formal symbolic representations are parsed and analyzed to extract the fundamental logical components and their relationships. Subsequently, these components are matched with their corresponding natural language expressions. The Result Interpreter must ensure that this matching accurately preserves the logical structure and meaning of the original symbolic answer, thereby upholding the accuracy and integrity of the reasoning process.

The incorporation of the Result Interpreter into the LOGIC-LM framework elevates the interpretability of the system’s outputs. Users can gain access to clear and succinct explanations of intricate logical inferences, which can prove particularly beneficial in applications like automated theorem proving, complex question answering, and semantic parsing. Through the transformation of symbolic solutions into natural language, the Result Interpreter ensures that the logical precision of the symbolic solver remains intact in the interpretation process.
Furthermore, the Result Interpreter plays a significant role in the iterative refinement process. By offering natural language feedback on the results produced by the symbolic solver, it can aid in identifying ambiguities or inconsistencies in the initial problem formulation. This feedback can then be utilized to iteratively refine and enhance the symbolic representation, ultimately leading to more precise and coherent final outputs.

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

# Multi-modal Logic Reasoning
In a multi-modal setting, not only textual data is given to the LLM, but also other structures of data, such as images, can be utilized as input. The LLM needs to extract the important information from the input data to be able to reason about it.

## Datasets Multi-modal
The multi-modal logic reasoning experiments were conducted by building synthetic datasets for Sudoku and Graph Coloring problems. Different datasets were created based on graphs, sudoku's and the SET card games. A textual prompt is also given to specify the task and the desired output format.

| Dataset name | Model's task | Logic representation & solver | Example input image |
| :-----------------------------: | :------------------------------: | :------------------------------: |:------------------------------: |
| **Graph Fill-in** | Filling in the missing color in a graph so that no two adjacent nodes have the same color. | ASP & Clingo | <img src="./media/graph_fill_in.png" width="300"> |
| **Graph Validity** | Determining whether it is possible to color a graph with a given set of colors such that no two adjacent nodes have the same color. | ASP & Clingo | <img src="./media/graph_validity.png" width="300"> |
| **Sudoku Fill-in** | Filling in the missing numbers in a Sudoku puzzle. | ASP & Clingo | <img src="./media/sudoku_fill_in.png" width="300">   |
| **Sudoku Validity** | Determining whether a given Sudoku puzzle is valid. | ASP & Clingo | <img src="./media/sudoku_validity.png" width="300"> |
| **SET** | Following the card game rules, find the sets given the cards shown in the image. The same cards can appear and are counted as a set. | ASP & Clingo | <img src="./media/SET.png" width="300"> |

Validity datasets contained 400 samples, with 200 valid and 200 invalid examples each. For fill-in problems, 200 samples were created. Validity problems had two possible answers (Yes, No) and Fill-in problems had four different options (for Sudoku, possible missing numbers; for graph, missing colors). For multiple choice problems, we employed ASP programs to ensure that there is only one correct answer by validating models count.

The datasets were created by combining textual and visual inputs. The textual inputs were generated by converting the logical problems into natural language descriptions, while the visual inputs were created by visualizing the logical problems. Models were prompted with both the textual and visual inputs to solve the problems, employing a one-example in-context learning strategy in all cases.

For direct prompting, models were given a sample question, an accompanying picture, and the correct answer. For ASP prompting, models were given a sample question, an accompanying picture, an ASP program that represents the problem, and the correct answer.

## ASP as symbolic language
We utilized an additional symbolic language to represent the multi-modal logic problems, namely Answer Set Programming (ASP). This language is more restricted than First-Order Logic (FOL), but is simpler to program. Its programs can be solved using Clingo.  Below, an example program is given, which is used for the Graph Fill-in dataset.

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

## Results Multi-modal

We evaluated the multi-modal LLM from the Gemini family `gemini-1.5-pro-preview-0409` using both ASP and direct prompting strategies. To validate the ASP-generated code, we employed the Clingo solver. The results are summarized below:

<table class="tg"><thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-c3ow" colspan="4">Accuracy % for prompting type</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Dataset<br></td>
    <td class="tg-c3ow">Direct <br><span style="font-weight:bold">Gemini Pro</span></td>
    <td class="tg-c3ow">Direct<br><span style="font-weight:bold">Gemini Flash</span></td>
    <td class="tg-c3ow">ASP<br><span style="font-weight:bold">Gemini Pro</span></td>
    <td class="tg-c3ow">ASP<br><span style="font-weight:bold">Gemini Flash</span></td>
  </tr>
  <tr>
    <td class="tg-0pky">Sudoku Fill-in</td>
    <td class="tg-0pky">28.50</td>
    <td class="tg-0pky">25.51</td>
    <td class="tg-0pky">67.50</td>
    <td class="tg-0pky">22.00</td>
  </tr>
  <tr>
    <td class="tg-0pky">Sudoku Validity</td>
    <td class="tg-0pky">48.00</td>
    <td class="tg-0pky">48.03</td>
    <td class="tg-0pky">92.08</td>
    <td class="tg-0pky">0.930</td>
  </tr>
  <tr>
    <td class="tg-0pky">Graph Fill-in</td>
    <td class="tg-0pky"42.52</td>
    <td class="tg-0pky">29.50</td>
    <td class="tg-0pky">65.01</td>
    <td class="tg-0pky">38.21</td>
  </tr>
  <tr>
    <td class="tg-0pky">Graph Validity</td>
    <td class="tg-0pky">53.51</td>
    <td class="tg-0pky">54.00</td>
    <td class="tg-0pky">94.50</td>
    <td class="tg-0pky">90.50</td>
  </tr>
  <tr>
    <td class="tg-0pky">SET Validity</td>
    <td class="tg-0pky">58.00</td>
    <td class="tg-0pky">55.51</td>
    <td class="tg-0pky">67.00</td>
    <td class="tg-0pky">48.51</td>
  </tr>
</tbody></table>


As we can see from the results, the model achieves much higher accuracy when prompted with ASP programs compared to direct prompting. This indicates that the model is able to better understand the logical problems when provided with the ASP programs, which are more structured and explicit compared to direct prompts.

While analyzing the mistakes made by the model using direct prompting, we observed that the model often struggled to correctly understand the logical problems, leading to incorrect answers and increased hallucinations.

For the ASP prompting, the primary mistakes made by the model were related to generating the problem representation as a valid ASP program. As the provided ASP programs required precise encoding of either Sudoku boards or graph coloring problems, the model often failed to generate correct ASP programs. This was especially evident in the Graph Fill-in problem, where the model struggled to correctly encode the graph coloring problem.

## Prompting - Ablation Experiments - In Context Learning ##

We evaluated the LLama family of models,ie- `meta-llama/Llama-2-7b-chat-hf` and `meta-llama/Meta-Llama-3-8B-Instruct`. In general, LLama3 performs way better than LLama2. The results table below are conducted wrt Llama3. We found that for logical tasks, where we have to predict one option out of 5 available options, the model is somewhat biased towards predicting the first choice. Additionally, if we allow to generate more tokens by increaisng the max_new_tokens hyper-parmater,ie- increasing  the maximum number of tokens to generate, the quality of the logic programs gets better. Additionally, we also performed an experiment when we prompted the model to predict all the incorrect options. We get higher accuracy in this case since we have 4 incorrect choices and 1 correct choice per sample. So, predicing a wrong answer is easier compared to the correct one.

|     Dataset     | Prompting | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :-------------: | :-------: | :------: |
| AR-LSAT Baseline  |  Direct   |   19.56   |
| AR-LSAT Swap the correct answer always to first choice |  Direct   |  25   |
| AR-LSAT Predict wrong answer choices  |  Direct   |   26   |


Additionally, below table demonstrates the Direct, CoT and Logic-LM results on all datasets with Llama3(meta-llama/Meta-Llama-3-8B-Instruct):

|     Dataset     | Prompting | Accuracy ( % for meta-llama/Meta-Llama-3-8B-Instruct ) |
| :-------------: | :-------: | :------: |
| ProntoQA   |  Direct ( 16 max_new_tokens )   |  43    |
| ProntoQA  |  CoT ( 1024 max_new_tokens )   | 76.6   |
| ProntoQA  |  Logic-LM (random backup strategy )   | 55    |
| ProntoQA  |  Logic-LM (Direct-Logic collabration mode (LLM) backup strategy )   | 42.46 |
| ProntoQA  |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   | 8    |
| ProofWriter   |  Direct ( 16 max_new_tokens )  |  33    |
| ProofWriter  |  CoT ( 1024 max_new_tokens )   | 28.54    |
| ProofWriter  |  Logic-LM (random backup strategy )  |  28.7   |
| ProofWriter  |  Logic-LM (Direct-Logic collabration mode (LLM) backup strategy )  |  28.69   |
| ProofWriter  |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )  |  28.695   |
| FOLIO   |  Direct ( 16 max_new_tokens )  | 46.5     |
| FOLIO  |  CoT ( 1024 max_new_tokens )    |   36  |
| FOLIO  |  Logic-LM (random backup strategy )   |   43  |
| FOLIO  |  Logic-LM (Direct-Logic collabration mode (LLM) backup strategy )   |   53  |
| FOLIO  |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )   |   44.285  |
| LogicalDeduction   |  Direct ( 16 max_new_tokens )  |   32.33   |
| LogicalDeduction  |  CoT ( 1024 max_new_tokens )    |  22   |
| LogicalDeduction  |  Logic-LM (random backup strategy )  |  24.27   |
| LogicalDeduction  |  Logic-LM (Direct-Logic collabration mode (LLM) backup strategy )  |  31   |
| LogicalDeduction  |  Logic-LM (CoT-Logic collabration mode (LLM) backup strategy )  |  20.38   |
| AR-LSAT   |  Direct ( 16 max_new_tokens )  | 7.36     |
| AR-LSAT  |  CoT ( 1024 max_new_tokens )    |  8.225   |
| AR-LSAT  |  Logic-LM  (random backup strategy ) |  22   |
| AR-LSAT  |  Logic-LM  (Direct-Logic collabration mode (LLM) backup strategy ) |  12   |
| AR-LSAT  |  Logic-LM  (CoT-Logic collabration mode (LLM) backup strategy ) |  6   |

## Gemini results

evaluation logic programs per task with backup option 'random':

|ProntoQA|gemini-1.0-pro-vision-001|gemini-1.5-pro-preview-0409|gemini-1.5-pro-preview-0514|gemini-1.5-flash-preview-0514|
 |---|---|---|---|---|
|Overall_Accuracy|77.40|95.60|46.40|46.94|
|Executable_Rate|100.00|96.40|0.00|0.00|
|Executable_Accuracy|77.40|97.30|0.00|0.00|

|ProofWriter|gemini-1.0-pro-vision-001|gemini-1.5-pro-preview-0409|gemini-1.5-pro-preview-0514|gemini-1.5-flash-preview-0514|
 |---|---|---|---|---|
|Overall_Accuracy|61.27|74.66|34.50|32.17|
|Executable_Rate|64.44|89.36|0.00|4.67|
|Executable_Accuracy|76.17|80.53|0.00|53.57|

|FOLIO|gemini-1.0-pro-vision-001|gemini-1.5-pro-preview-0409|gemini-1.5-pro-preview-0514|gemini-1.5-flash-preview-0514|
 |---|---|---|---|---|
|Overall_Accuracy|53.00|62.38|71.14|36.27|
|Executable_Rate|48.50|59.41|77.11|4.41|
|Executable_Accuracy|68.04|82.50|85.16|100.00|

|LogicalDeduction|gemini-1.0-pro-vision-001|gemini-1.5-pro-preview-0409|gemini-1.5-pro-preview-0514|gemini-1.5-flash-preview-0514|
 |---|---|---|---|---|
|Overall_Accuracy|61.33|60.33|84.67|56.33|
|Executable_Rate|60.00|60.00|100.00|71.67|
|Executable_Accuracy|89.44|87.22|84.67|69.77|

|AR-LSAT|gemini-1.0-pro-vision-001|gemini-1.5-pro-preview-0409|gemini-1.5-pro-preview-0514|gemini-1.5-flash-preview-0514|
 |---|---|---|---|---|
|Overall_Accuracy|22.17|19.05|31.60|32.47|
|Executable_Rate|0.00|0.00|26.41|33.77|
|Executable_Accuracy|0.00|0.00|60.66|60.26|


Evaluation baselines with Gemini. All baselines results (Direct and CoT) are done with gemini-1.5-flash-preview-0514. Best accuracy score of the Logic-LM approach with the random backup strategy is presented for comparison.:

| dataset | mode | accuracy | best model
| --- | --- | --- | --- |
| ProntoQA | Direct | 63.80 | - |
| - | CoT | 92.34  | - |
| - | Logic-LM | 95.60 | gemini-1.5-pro-preview-0409 |
| ProofWriter | Direct | 53.83 | - |
| - | CoT | 65.15 | - |
| - | Logic-LM | 74.66 | gemini-1.5-pro-preview-0409 |
| FOLIO | Direct | 66.67 | - |
| - | CoT | 49.25 | - |
| - | Logic-LM | 71.14 | gemini-1.5-pro-preview-0514 |
| LogicalDeduction | Direct | 54.67 | - |
| - | CoT | 30.00 | - |
| - | Logic-LM | 84.67 | gemini-1.5-pro-preview-0514 |
| AR-LSAT | Direct | 27.95 | - |
| - | CoT | 20.35 | - |
| - | Logic-LM | 32.47 | gemini-1.5-flash-preview-0514 |


## Concluding Remarks

TODO

## Student Contributions

Dominykas Šeputis and Chimène Blokesch focused primarily on multi-modal foundation models to assess their ability to address logical issues using both textual and visual inputs. Soham Chatterjee delved into how LLMs behave to different prompting approaches, such as Direct, Chain of Thought, Few shot inluding more prompt examples, investigated the effectiveness by forcing LLMs to output incorrect choices and performed extensive ablation studies with 5 different datasets, each corresponding to a logical task with Direct, Chain of Thought and Logic-LM approaches. Job Gräber led the adaptation of LLMs for logic problem-solving through fine-tuning methods. Idries Nasim primarily oversaw the coordination of experiments and the drafting of the research report, also providing assistance with ablation studies as needed. All team members made active contributions by presenting the results of their experiments.

## Bibliography
