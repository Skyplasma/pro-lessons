raw_text = (
    "  Python   is   powerful, flexible, and easy to learn.\n"
    "Many   beginners    enjoy  Python because it reads well.\n"
    "PYTHON  code   is often used  for scripting, data work, and teaching.   "
)
newlinetext = raw_text.split("/n")
split_text = raw_text.split()
print(newlinetext)
normal_text = " ".join(split_text)
done_text = normal_text.capitalize()
print(done_text)