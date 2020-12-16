# 1. Pengalaman saya mengunakan Python untuk mengolah data dan pemodelan Matematika untuk kuliah selama 1 tahun belakangan ini, saya juga mengunakan python untuk berbagai macam proyek individu.
# 2. Saya Berharap dapat meningkatkan kemampuan anlisis data saya setelah menjalani kelas lanjutan ini

class Manipulasi:

    def __init__(self,string):
        if type(string) != str:
            raise TypeError(f"Cannot initialize a string of type{type(string)}")
        self.sentence = string
    
    def to_word_list(self):
        return self.sentence.split(" ")
    
    def capitalize_each_letter(self):
        sentence = list(self.sentence)
        for letter in sentence:
            letter = letter.upper()
        return ''.join(sentence)
    
    def capitalize_first_letter(self):
        sentence = list(self.sentence)
        sentence[0] = sentence[0].upper()
        return ''.join(sentence)
    
    def lower_case_each_letter(self):
        sentence = list(self.sentence)
        for letter in sentence: 
            letter = letter.lower()
        return ''.join(sentence) 


if __name__ == "__main__":
    data = Manipulasi("saya tinggal di Indonesia")
    print(data.capitalize_first_letter())
    print(data.lower_case_each_letter())
    print(data.capitalize_each_letter())
    print(data.to_word_list())
