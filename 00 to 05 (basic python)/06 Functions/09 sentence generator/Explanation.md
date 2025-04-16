# 🧠 Logic Recap: Sentence Generator

Function / Variable        : What It Represents                            : User Input? : Explanation
---------------------------------------------------------------------------------------------------------
make_sentence(...)         : Generates a sentence with the input word      : ❌ No        : Called by `main()` after input
word                       : The word to insert into a sentence            : ✅ Yes       : e.g., "groovy", "run", "cloud"
part_of_speech             : Integer indicating part of speech             : ✅ Yes       : 0 = noun, 1 = verb, 2 = adjective
if part_of_speech == 0     : Sentence for noun                             : ❌ No        : Uses noun template
elif part_of_speech == 1   : Sentence for verb                             : ❌ No        : Uses verb template
elif part_of_speech == 2   : Sentence for adjective                        : ❌ No        : Uses adjective template
print(...)                 : Displays generated sentence                   : ❌ No        : Based on selected template
