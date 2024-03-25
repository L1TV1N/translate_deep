from deep_translator import GoogleTranslator
import csv
import chardet

def translate_text(input_text):
    translated_text = GoogleTranslator(source='ru', target='en').translate(input_text)
    return translated_text

def translate_csv(input_file, output_txt_file, output_csv_file):
    # Определение кодировки файла
    with open(input_file, 'rb') as f:
        rawdata = f.read()
    encoding = chardet.detect(rawdata)['encoding']

    # Чтение файла CSV с определенной кодировкой
    with open(input_file, 'r', encoding=encoding) as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)  # Читаем заголовки
        translated_rows = []
        for row in reader:
            translated_row = [translate_text(cell) for cell in row]
            translated_rows.append(translated_row)

    # Сохраняем в txt файл
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        for row in translated_rows:
            txt_file.write(','.join(row) + '\n')

    # Сохраняем в csv файл
    with open(output_csv_file, 'w', encoding='utf-8', newline='') as csv_output_file:
        writer = csv.writer(csv_output_file)
        writer.writerow(headers)
        writer.writerows(translated_rows)

if __name__ == "__main__":
    input_csv_file = 'trasckription.csv'  # Имя входного CSV файла
    output_txt_file = 'output.txt'  # Имя выходного txt файла
    output_csv_file = 'output.csv'  # Имя выходного CSV файла
    translate_csv(input_csv_file, output_txt_file, output_csv_file)
