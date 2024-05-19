# generate facts and rules based on the problem description

import json
import os
from tqdm import tqdm
from collections import OrderedDict
from typing import Dict, List, Tuple
from utils import OpenAIModel, GenimiModel,LamaModel
import argparse

import model_globals


class LogicProgramGenerator:
    def __init__(self, args):
        self.args = args
        self.data_path = args.data_path
        self.dataset_name = args.dataset_name
        self.split = args.split
        self.model_name = args.model_name
        self.save_path = args.save_path

        if self.model_name in model_globals.GEMINI_MODEL_NAMES:
            self.LLM = GenimiModel(args.model_name, args.stop_words, args.max_new_tokens)
        elif self.model_name in model_globals.LAMA_MODEL_NAMES:
            print("Lama Model")
            self.LLM = LamaModel(args.model_name, args.max_new_tokens)
            #print("HERE 13")
        else:
            self.LLM = OpenAIModel(args.api_key, args.model_name, args.stop_words, args.max_new_tokens)


        self.prompt_creator = {'FOLIO': self.prompt_folio,
                               'ProntoQA': self.prompt_prontoqa,
                               'ProofWriter': self.prompt_proofwriter,
                               'LogicalDeduction': self.prompt_logicaldeduction, 
                               'AR-LSAT': self.prompt_arlsat}
        self.load_prompt_templates()
    
    def load_prompt_templates(self):
        #print("HERE 12")
        prompt_file = f'./models/prompts/{self.dataset_name}.txt'
        # if self.dataset_name == 'AR-LSAT' and self.model_name == 'gpt-4':
        if self.dataset_name == 'AR-LSAT' and self.model_name in model_globals.MODEL_LARGE_CONTEXT:
            prompt_file = f'./models/prompts/{self.dataset_name}-long.txt'
        with open(prompt_file, 'r') as f:
            self.prompt_template = f.read()

    def prompt_folio(self, test_data):
        message = []
        
    
        d = {}
        d["role"] = "user"

        problem = test_data['context']
        question = test_data['question'].strip()
        full_prompt = self.prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)

        d["content"]  = full_prompt
        message.append(d)
        return message

    def prompt_arlsat(self, test_data):
        message = []
        
    
        d = {}
        d["role"] = "user"
      
   
    
        problem = test_data['context']
        question = test_data['question'].strip()
        choices_str = '\n'.join([f'({choice.strip()}' for choice in test_data['options']]).strip()
        full_prompt = self.prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        full_prompt = full_prompt.replace('[[CHOICES]]', choices_str)
        d["content"]  = full_prompt
        message.append(d)
    
        return message
    
    def prompt_prontoqa(self, test_data):
        message = []
        d = {}
        d["role"] = "user"
        problem = test_data['context']
        question = test_data['question'].strip()
        full_prompt = self.prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        d["content"]  = full_prompt
        message.append(d)
        return message
    
    def prompt_proofwriter(self, test_data):
        message = []
        
    
        d = {}
        d["role"] = "user"
        problem = test_data['context']
        question = test_data['question'].strip()
        full_prompt = self.prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)

        d["content"]  = full_prompt
        message.append(d)
        return message
    
    def prompt_logicaldeduction(self, test_data):
        message = []
        
    
        d = {}
        d["role"] = "user"

        problem = test_data['context']
        question = test_data['question'].strip()
        choices_str = '\n'.join([f'({choice.strip()}' for choice in test_data['options']]).strip()
        full_prompt = self.prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        full_prompt = full_prompt.replace('[[CHOICES]]', choices_str)

        d["content"]  = full_prompt
        message.append(d)
        return message

    def load_raw_dataset(self, split):
        with open(os.path.join(self.data_path, self.dataset_name, f'{split}.json')) as f:
            raw_dataset = json.load(f)
        return raw_dataset

    def logic_program_generation(self):
        # load raw dataset
        raw_dataset = self.load_raw_dataset(self.split)
        print(f"Loaded {len(raw_dataset)} examples from {self.split} split.")

        outputs = []
        for example in tqdm(raw_dataset):
            # create prompt
            # try:
            #     full_prompt = self.prompt_creator[self.dataset_name](example)
            #     output = self.LLM.generate(full_prompt)
            #     programs = [output]

            #     # create output
            #     output = {'id': example['id'], 
            #             'context': example['context'],
            #             'question': example['question'], 
            #             'answer': example['answer'],
            #             'options': example['options'],
            #             'raw_logic_programs': programs}
            #     outputs.append(output)
            full_prompt = self.prompt_creator[self.dataset_name](example)
            output = self.LLM.generate(full_prompt)
            programs = [output]

            # create output
            output = {'id': example['id'], 
                    'context': example['context'],
                    'question': example['question'], 
                    'answer': example['answer'],
                    'options': example['options'],
                    'raw_logic_programs': programs}
            outputs.append(output)
            with open(os.path.join(self.save_path, f'{self.dataset_name}_{self.split}_{self.model_name}.json'), 'w') as f:
                json.dump(outputs, f, indent=2, ensure_ascii=False)
            

        # save outputs
        print("Outputs:",outputs)        
        with open(os.path.join(self.save_path, f'{self.dataset_name}_{self.split}_{self.model_name}.json'), 'w') as f:
            json.dump(outputs, f, indent=2, ensure_ascii=False)

    '''
    Updated version of logic_program_generation; speed up the generation process by batching
    '''
    def batch_logic_program_generation(self, batch_size = 10):
        #print("HERE 11")
        # load raw dataset
        raw_dataset = self.load_raw_dataset(self.split)
        print(f"Loaded {len(raw_dataset)} examples from {self.split} split.")

        outputs = []
        # split dataset into chunks
        dataset_chunks = [raw_dataset[i:i + batch_size] for i in range(0, len(raw_dataset), batch_size)]
        for chunk in tqdm(dataset_chunks):
            # create prompt
            full_prompts = [self.prompt_creator[self.dataset_name](example) for example in chunk]
            #print(full_prompts)
            try:
                # if self.model_name in model_globals.LAMA_MODEL_NAMES:
                #     # our code for batching with gemini doesn't work yet 
                #     raise Exception("our code for batching with gemini doesn't work yet ")
                batch_outputs = self.LLM.generate(full_prompts)
                print(batch_outputs)
                # create output
                for sample, output in zip(chunk, batch_outputs):
                    programs = [output]
                    output = {'id': sample['id'], 
                            'context': sample['context'],
                            'question': sample['question'], 
                            'answer': sample['answer'],
                            'options': sample['options'],
                            'raw_logic_programs': programs}
                    outputs.append(output)
            except:
                # generate one by one if batch generation fails
                for sample, full_prompt in zip(chunk, full_prompts):
                    try:
                        output = self.LLM.generate(full_prompt)
                        programs = [output]
                        output = {'id': sample['id'], 
                                'context': sample['context'],
                                'question': sample['question'], 
                                'answer': sample['answer'],
                                'options': sample['options'],
                                'raw_logic_programs': programs}
                        outputs.append(output)
                    except:
                        print('Error in generating logic programs for example: ', sample['id'])

        # remove examples with duplicate ids from the result
        outputs = list({output['id']: output for output in outputs}.values())
        print("Outputs:",outputs)
        print(f"Generated {len(outputs)} examples.")
        
        # save outputs
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        
        with open(os.path.join(self.save_path, f'{self.dataset_name}_{self.split}_{self.model_name}.json'), 'w') as f:
            json.dump(outputs, f, indent=2, ensure_ascii=False)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='./data')
    parser.add_argument('--dataset_name', type=str)
    parser.add_argument('--split', type=str, default='dev')
    parser.add_argument('--save_path', type=str, default='./outputs/logic_programs')
    parser.add_argument('--api_key', type=str)
    parser.add_argument('--model_name', type=str, default='lama3')
    parser.add_argument('--stop_words', type=str, default='------')
    parser.add_argument('--max_new_tokens', type=int, default=1024)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    logic_program_generator = LogicProgramGenerator(args)
    logic_program_generator.logic_program_generation()