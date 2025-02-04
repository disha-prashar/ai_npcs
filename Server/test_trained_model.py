from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
class model:
    def chat_with_model(input):
        local_model_directory = "C:/Users/NomadXR/Desktop/mistral_4470/zephyr_model"
        model = AutoModelForCausalLM.from_pretrained(local_model_directory) #.to('cuda') #(model_name, device_map="auto", trust_remote_code=False,revision="main")
        tokenizer = AutoTokenizer.from_pretrained(local_model_directory, use_fast=True, src_lang="en")
        
        initialPrompt = "please act like a potion seller"
        input_ids = tokenizer.encode(initialPrompt, return_tensors="pt") #.input_ids.cuda()
        generate_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, temperature=0.9, do_sample=True) #top_p=0.95, top_k=40, max_new_tokens=512
        print(tokenizer.decode(generate_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False))

        while True:
            # prompt = input("\nEnter prompt: ") #"What's the capital of Australia?"  "Who is Scott McCall?" "Act like a potion seller." "Can you tell me about your transformation?"
            # prompt_template=f'''{prompt}'''

            if input == "exit":
                break
            
            input_ids = tokenizer.encode(input, return_tensors="pt") #.input_ids.cuda()

            # print("\n*** Generate:\n")
            generate_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, temperature=0.9, do_sample=True) #top_p=0.95, top_k=40, max_new_tokens=512
            modelResponse = tokenizer.decode(generate_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
            modelResponseParsed = modelResponse.split("|>")
            modelResponseParsed = modelResponseParsed[1]

            return modelResponseParsed
# if __name__ == "__main__":
    # initial_role = "be a potion seller"
    # chat_with_model(initial_role)


# decoded = tokenizer.batch_decode(output)
# print(decoded[0])


# messages = [
#     {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate",},
#     {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
# ]
# tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
# print(tokenizer.decode(tokenized_chat[0]))
# outputs = model.generate(tokenized_chat, max_new_tokens=128) 
# print(tokenizer.decode(outputs[0]))