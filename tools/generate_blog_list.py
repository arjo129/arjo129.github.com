import os
import markdown
from bs4 import BeautifulSoup
import re
from datetime import datetime
from jinja2 import Template


from podgen import Podcast, Episode
import pytz
from datetime import datetime, timezone

def generate_rss_feed(blog_entries):
    p = Podcast(
        name="Arjo's Blog",
        description="Personal blog of Arjo Chakravarty",
        website="https://arjo129.github.io",
        explicit=False,
        language="en-US"
    )
    
    for entry in blog_entries:
        # Create episode (entry)
        episode = Episode(
            title=entry['title'],
            summary=entry['summary'],
            publication_date=entry['date'].replace(tzinfo=pytz.UTC),
            link=f'https://arjo129.github.io/blog/{entry["link"]}'
        )
        p.episodes.append(episode)
    
    # Generate the RSS feed file
    p.rss_file('blog/feed.xml', minimize=False)

def convert_md_to_html(markdown_content):
    # Configure markdown extensions
    md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'tables', 'toc'])
    return md.convert(markdown_content)

def get_blog_template():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
    <title>{{ title }} - Arjo's Blog</title>
  </head>
  <body>
    <!-- Navbar will be loaded here -->
    <header></header>

    <div class="container mt-5">
      <article class="blog-post">
        <p class="text-muted">{{ date }}</p>
        {{ content }}
      </article>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
    <!-- Load navbar -->
    <script src="/navbar.js"></script>
  </body>
</html>
'''
def process_blog_posts():
    blog_entries = []
    blog_dir = "blog"
    
    # Create blog directory if it doesn't exist
    os.makedirs(blog_dir, exist_ok=True)
    
    # Get all markdown files from the blog directory
    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(blog_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert markdown to HTML
            html_content = convert_md_to_html(content)
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Get title (first h1)
            title = soup.find('h1')
            title = title.text if title else 'Untitled'
            
            # Get first paragraph
            first_para = soup.find('p')
            summary = first_para.text if first_para else 'No summary available'
            
            # Get date from filename (assuming format: YYYY-MM-DD-title.md)
            date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
            if date_match:
                date_str = date_match.group(1)
                date = datetime.strptime(date_str, '%Y-%m-%d')
            else:
                date = datetime.fromtimestamp(os.path.getctime(file_path))
            
            # Generate HTML file name
            html_filename = filename.replace('.md', '.html')
            
            # Create individual blog post HTML
            template = Template(get_blog_template())
            blog_html = template.render(
                title=title,
                date=date.strftime('%B %d, %Y'),
                content=html_content
            )
            
            # Save individual blog post HTML
            with open(os.path.join(blog_dir, html_filename), 'w', encoding='utf-8') as f:
                f.write(blog_html)
            
            blog_entries.append({
                'title': title,
                'summary': summary,
                'date': date,
                'link': html_filename
            })
    
    # Sort by date, newest first
    return sorted(blog_entries, key=lambda x: x['date'], reverse=True)

def generate_blog_index(blog_entries):
    html_content = []
    
    for entry in blog_entries:
        entry_html = f'''
        <div class="card mb-4">
            <div class="card-body">
                <h2 class="card-title">{entry['title']}</h2>
                <h6 class="card-subtitle mb-2 text-muted">{entry['date'].strftime('%B %d, %Y')}</h6>
                <p class="card-text">{entry['summary']}</p>
                <a href="blog/{entry['link']}" class="btn btn-primary">Read More</a>
            </div>
        </div>
        '''
        html_content.append(entry_html)
    
    return '\n'.join(html_content)

def get_blog_index_template():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="alternate" type="application/rss+xml" title="Arjo's Blog RSS Feed" href="/blog/feed.xml">
    <title>Blog - Arjo Chakravarty</title>
  </head>
  <body>
    <!-- Navbar will be loaded here -->
    <header></header>

    <div class="container mt-5">
      <div class="row">
        {% for entry in blog_entries %}
        <div class="card mb-4">
            <div class="card-body">
                <h2 class="card-title">{{ entry.title }}</h2>
                <h6 class="card-subtitle mb-2 text-muted">{{ entry.date.strftime('%B %d, %Y') }}</h6>
                <p class="card-text">{{ entry.summary }}</p>
                <a href="blog/{{ entry.link }}" class="btn btn-primary">Read More</a>
            </div>
        </div>
        {% endfor %}
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Load navbar -->
    <script src="navbar.js"></script>
  </body>
</html>
'''

# Update the main execution block:
if __name__ == "__main__":
    # Process blog posts and get entries
    blog_entries = process_blog_posts()
    print(blog_entries)
    
    # Generate RSS feed
    generate_rss_feed(blog_entries)
    
    # Generate blog index using Jinja template
    template = Template(get_blog_index_template())
    blog_html = template.render(blog_entries=blog_entries)
    
    # Write the final HTML
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)