# EX 3.1 Write a function preprocess that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
# Write a function preprocess_file(input_file_path, output_file_path) that reads a file, breaks each line into words, strips whitespace and punctuation from the words, converts them to lowercase, save the resulting texts.
#
# Write a program to test your function.
def prepocess_file(input_file_path, output_file_path):
    file_writer = open(output_file_path, 'w', encoding='utf-8')

    import string
    for line in open(input_file_path, encoding='utf-8').readlines():
        words = line.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
        file_writer.write(words)

    file_writer.close()

