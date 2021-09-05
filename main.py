#implement of bag of wrods in python
defvectorize(tokens):
&#39;&#39;&#39; This function takes list of words in a sentence as input
and returns a vector of size of filtered_vocab.It puts 0 if the
word is not present in tokens and count of token if present.&#39;&#39;&#39;
vector=[]
for w in filtered_vocab:
vector.append(tokens.count(w))
return vector
def unique(sequence):
&#39;&#39;&#39;This functions returns a list in which the order remains
same and no item repeats.Using the set() function does not
preserve the original ordering,soididnt use that instead&#39;&#39;&#39;
seen = set()
return [x for x in sequence if not (x in seen or seen.add(x))]
#create a list of stopwords.You can import stopwords from nltk too
stopwords=[&quot;to&quot;,&quot;is&quot;,&quot;a&quot;]
#list of special characters.You can use regular expressions too
special_char=[&quot;,&quot;,&quot;:&quot;,&quot; &quot;,&quot;;&quot;,&quot;.&quot;,&quot;?&quot;]
#Write the sentences in the corpus,in our case, just two
string1=&quot;It was the best of times&quot;
string2=&quot;It was the worst of times&quot;
#convert them to lower case
string1=string1.lower()
string2=string2.lower()
#split the sentences into tokens
tokens1=string1.split()
tokens2=string2.split()
print(tokens1)
print(tokens2)
#create a vocabulary list
vocab=unique(tokens1+tokens2)
print(vocab)
#filter the vocabulary list
filtered_vocab=[]
for w in vocab:
if w not in stopwords and w not in special_char:
filtered_vocab.append(w)
print(filtered_vocab)
#convert sentences into vectords
vector1=vectorize(tokens1)
print(vector1)
vector2=vectorize(tokens2)
print(vector2)
