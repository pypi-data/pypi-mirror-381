class PromptTemplate:
    placeholders = ["reference", "question"]
    base_system_prompt = (
        "Answer the question based on the given document."
        "Only give me the answer and do not output any other words."
        "\nThe following are given documents.\n\n{reference}"
    )
    base_user_prompt = "Question: {question}"

    def __init__(self, tokenizer, system_prompt="", user_prompt=""):

        self.max_input_len = 64000
        self.tokenizer = tokenizer

        if len(system_prompt) == 0 and len(user_prompt) == 0:
            system_prompt = self.base_system_prompt
            user_prompt = self.base_user_prompt
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.enable_chat = True
        self.is_chat = True
        self.is_openai = False
        self.reference_template = None

        # self._check_placeholder()

    def _check_placeholder(self):
        # check placeholder in prompt
        for holder in self.placeholders:
            flag = False
            for prompt in [self.system_prompt, self.user_prompt]:
                if f"{holder}" in prompt:
                    print(f"Find `{holder}` in template")
                    flag = True
                    break
            if not flag and holder != "reference":
                assert False

    def truncate_prompt(self, prompt):
        if self.is_openai:
            truncated_messages = []
            total_tokens = 0
            assert isinstance(prompt, list)
            for message in prompt:
                role_content = message["content"]
                encoded_message = self.tokenizer.encode(role_content)

                if total_tokens + len(encoded_message) <= self.max_input_len:
                    truncated_messages.append(message)
                    total_tokens += len(encoded_message)
                else:
                    print(
                        f"The input text length is greater than the maximum length ({total_tokens + len(encoded_message)} > {self.max_input_len}) and has been truncated!"
                    )
                    remaining_tokens = self.max_input_len - total_tokens
                    truncated_message = self.encoding.decode(
                        encoded_message[:remaining_tokens]
                    )
                    message["content"] = truncated_message
                    truncated_messages.append(message)
                    break

            return truncated_messages

        else:
            assert isinstance(prompt, str)
            tokenized_prompt = self.tokenizer(
                prompt, truncation=False, return_tensors="pt"
            ).input_ids[0]

            if len(tokenized_prompt) > self.max_input_len:
                print(
                    f"The input text length is greater than the maximum length ({len(tokenized_prompt)} > {self.max_input_len}) and has been truncated!"
                )
                half = int(self.max_input_len / 2)
                prompt = self.tokenizer.decode(
                    tokenized_prompt[:half], skip_special_tokens=True
                ) + self.tokenizer.decode(
                    tokenized_prompt[-half:], skip_special_tokens=True
                )
            return prompt

    def get_prompt(
        self,
        question=None,
        retrieval_result=None,
        formatted_reference=None,
        previous_gen=None,
        messages=None,
        **params,
    ):
        if messages is not None:
            if isinstance(messages, str):
                return self.truncate_prompt(messages)
            if self.is_chat and self.enable_chat:
                if self.is_openai:
                    self.truncate_prompt(messages)
                else:
                    prompt = self.tokenizer.apply_chat_template(
                        messages, tokenize=False, add_generation_prompt=True
                    )
                    return self.truncate_prompt(prompt)
            else:
                prompt = "\n\n".join(
                    [message["content"] for message in messages if message["content"]]
                )
                return self.truncate_prompt(prompt)

        if formatted_reference is None:
            if retrieval_result is not None:
                formatted_reference = self.format_reference(retrieval_result)
            else:
                formatted_reference = ""

        input_params = {"question": question, "reference": formatted_reference}
        input_params.update(**params)

        system_prompt = self.system_prompt.format(**input_params)
        user_prompt = self.user_prompt.format(**input_params)

        if self.is_chat and self.enable_chat:
            input = []
            if system_prompt != "":
                input.append({"role": "system", "content": system_prompt})
            if user_prompt != "":
                input.append({"role": "user", "content": user_prompt})
            if not self.is_openai:
                input = self.tokenizer.apply_chat_template(
                    input, tokenize=False, add_generation_prompt=True
                )
        else:
            input = "\n\n".join(
                [prompt for prompt in [system_prompt, user_prompt] if prompt != ""]
            )

        if (
            previous_gen is not None
            and previous_gen not in ["", " "]
            and self.is_openai is False
        ):
            input += previous_gen

        return self.truncate_prompt(input)

    def format_reference(self, retrieval_result):
        format_reference = ""
        for idx, doc_item in enumerate(retrieval_result):
            content = doc_item["contents"]
            title = content.split("\n")[0]
            text = "\n".join(content.split("\n")[1:])
            if self.reference_template is not None:
                format_reference += self.reference_template.format(
                    idx=idx, title=title, text=text
                )
            else:
                format_reference += f"Doc {idx + 1}(Title: {title}) {text}\n"

        return format_reference
