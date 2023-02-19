import openai
from deep_translator import GoogleTranslator
# Initialize the OpenAI API client
openai.api_key = "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"
while True:
    translateneed = 'yes'
    to_translate = input('Ваше сообщение: ')
    if to_translate[:3] == '---':
        translateneed = 'no'
        to_translate = to_translate[3:]
    print('Переводим ваше сообщение...')
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    print('Ожидание результата по переведённому запросу',translated + '...')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{str(translated)}",
        max_tokens=1024,
        frequency_penalty=0,
        presence_penalty=0,
        top_p=1,
        temperature=0.5
    ).choices[0].text
    # Translate the response to Russian
    if translateneed == 'yes':
        to_translate = response
        translated = GoogleTranslator(source='auto', target='ru').translate(to_translate)
    else: 
        translated = response
    # Send the translated text back to Console
    print(translated)