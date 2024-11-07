# Getting an LLM to write a blog engine

This is a blog engine that I wrote for my own website. It is powered by an LLM.
The llm was asked to generate the python script that pulls articles from the blog folder and displays the title and first paragraph of each article in the front page. It then provides a link to the full article. 

The source code for the blog engine is available [here](https://github.com/arjo129/arjo129.github.com/blob/master/tools/generate_blog_list.py). It's pretty crazy what AI can do with a little prompting. It took me about an hour to fix everything up (as someone who is not a webdev this feels great). I used the cursor editor to write the prompt and then copy the output into the python script. It was surprisingly productive, I might consider using this more in the future. 