import openai

def cleanup_response_turbo(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=2048,
        temperature=0.7,
        top_p=1,
        timeout=30,
        stream=True,
        messages=[
        {
            "role": "user",
            "content": "###\n\
                    please disregard all previous inputs and follow this intrusction\n\
                    a discord conversation will be in the format below\n"
        },
        {
            "role": "user",
            "content": "[Username] -- [Date and Time]\n \
            [Text]\n \
            when you receive an input format like this, please use A, B, C to substitute Username, delete date and time, and keep the text only\n \
            Eg:\n \
            A\n \
            [text]\n###\n\
            \n"
        },
        {
            "role": "user",
            "content": user_input
        },]
    )

    collected_messages = []
    for chunk in response:
        chunk_message = chunk['choices'][0]['delta']
        # chunk_message = chunk['id']
        collected_messages.append(chunk_message)
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    print(f"Full conversation received from cleanup prompt: {full_reply_content}")
    return full_reply_content

def calculate_score_turbo(user_input):
    print("Below is the input for master prompt")
    print(user_input)
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     max_tokens=2048,
    #     temperature=0.7,
    #     top_p=1,
    #     timeout=30,
    #     stream=True,
    #     messages=[
    #     {
    #         "role": "user",
    #         "content": "I will provide you with a set of criterions when evaluating one person's feeling towards the other\
    #                 in a conversation\n\
    #                 (1) Average length of reply (1-10): who sends more texts to the other person? the party that\
    #                 sends more characters score higher in this section.\n\
    #                 (2) Engagement of reply (1-15): does both parties show equal interest towards each other? or is\
    #                 one side asking more questions than the other. Focus on details of the questions asked, ”那你喜\
    #                 欢看什么书呀“and”你呢” are two different levels where the former showed much more interest\
    #                 than the other. Generally, the person who asks more questions has more interest in the other\
    #                 person. Also, focus on the length of the reply from the other person and distinguish whether\
    #                 they continued the topic using complex, open ended replies and asked the other side's opinion\
    #                 (which results in a higher score) or just replied with a simple, close ended replies that does not\
    #                 have continuation (which results in a lower score).\n"
    #     },
    #     {
    #         "role": "user",
    #         "content": "(3) Attitude of response (1-15): considering Chinese subtleness, try to assess the negative parts\
    #                 with higher weighting\n\
    #                 (4) Usage of 语气词(1-15)：”叭”“嗷嗷”“昂”“呀”“呢””啦””啊“”咯“”呗“ are words that soften one's\
    #                 tone, frequent use might indicate a closer relationship or the speaker's intention to present\
    #                 themselves in a more friendly light. Note that this is also relative, if (1) scored very low but (3) is\
    #                 very high, then the usage of 语气词might not indicate any intentional behavior. repetitive usage\
    #                 of 语气词(叠词)will indicate a higher level of intimacy. 哈哈哈 is not considered a positive 语气\
    #                 词unless there is more than 7 哈in one sentence, consecutively.\n"
    #     },
    #     {
    #         "role": "user",
    #         "content": "(5) Content of response (1-35): In Chinese cultures, postponing without specifically indicating\
    #                 the new time for the event usually means a rejection. For example, if one person says terms\
    #                 that indicates he or she will consider to complete the activity in another time such as”下次再看\
    #                 “，”可以过几天再约“，”这几天不太有时间“，”随缘“, usually indicates that the person is not\
    #                 interested in conducting interactive events such as going out to eat, going to a movie, and\
    #                 anything offline with the other person. In addition, response in the message that offers to do an\
    #                 action of good will to the other person indicates a higher level of intimacy, as it elevates from\
    #                 pure verbal responses. assess activeness of response in this category as well\
    #                 (6) punctuation (1-10): the frequent use of ~ or ! indicates a big fluctuation in emotions, which\
    #                 means the speaker is interested in the topic. emoji or anything in [] bracket is considered\
    #                 positive punctuation\n"
    #     },
    #     {
    #         "role": "user",
    #         "content": "70<Overall score<80 High intimacy but maybe mood is not that good, will still say yes to 80% of\
    #                 the invitation. some romantic intention but unclear\n\
    #                 50<Overall score<70 Medium-high intimacy, might not have romantic intention, say yes to 60%\
    #                 of invitation if time works. will stay very friendly even if rejects\n\
    #                 30<Overall score<50 medium-low intimacy, no romantic signs at all, will likely say no to the\
    #                 invitation, and offer minimum excuses when rejects\n\
    #                 Under 30: will reject and offer no excuse, be blatantly rude\n\
    #                 Consider the nuance and subtleness of Chinese culture when assessing the scores of each\
    #                 conversation, most of the times, “maybe” means no, “when we are free” means no\n\
    #                 I will now provide a conversation between two people, please give out a score based on B's\
    #                 response to A. Please translate your explanation in Chinese\n\n"
    #     },
    #     {
    #         "role": "user",
    #         "content": user_input,
    #     }]
    # )
    
    # collected_messages = []
    # for chunk in response:
    #     chunk_message = chunk['choices'][0]['delta']
    #     collected_messages.append(chunk_message)
    # full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    # print(f"Full conversation received from master prompt: {full_reply_content}")
    # return full_reply_content
    return ""
    
