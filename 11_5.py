def calculate_average_word_length(words):
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if len(words) > 0 else 0

def calculate_average_sentence_length(sentences):
    total_length = sum(len(sentence) for sentence in sentences)
    return total_length / len(sentences) if len(sentences) > 0 else 0

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Split the text into words
        words = text.split()

        # Remove punctuation from words
        words = [word.strip(string.punctuation) for word in words]

        # Split the text into sentences
        sentences = text.split('.')

        # Calculate average word length
        avg_word_length = calculate_average_word_length(words)

        # Calculate average sentence length
        avg_sentence_length = calculate_average_sentence_length(sentences)

        # Print results
        print(f"Average Word Length: {avg_word_length:.2f} characters")
        print(f"Average Sentence Length: {avg_sentence_length:.2f} characters")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    main(file_path)
