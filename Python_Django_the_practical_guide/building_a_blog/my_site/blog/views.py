from django.shortcuts import render
from datetime import date

all_posts = [
  {
    "slug": "trump-asia-summit-xi-jinping",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Trump in Asia for High-Stakes Xi Summit",
    "excerpt": "US President Trump is in Tokyo for key trade and security talks, laying the groundwork for a critical meeting with Chinese President Xi Jinping.",
    "content": """
      All eyes are on Asia as US President Trump lands in Tokyo for critical trade and security discussions with Japan's new prime minister. This visit is seen as the prelude to a high-stakes summit with Chinese President Xi Jinping.
      
      Reports suggest an "early consensus" on some trade issues might be forming, though significant tensions remain. Just ahead of the talks, China's military flew bombers near Taiwan, while its Foreign Minister, Wang Yi, delivered a major speech in Beijing calling for stronger "global governance" and multilateralism, setting a complex stage for the upcoming meeting.
    """
  },
  {
    "slug": "hurricane-melissa-category-4-caribbean",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Hurricane Melissa Becomes 'Catastrophic' Cat 4",
    "excerpt": "Jamaica and Haiti are bracing for impact as Hurricane Melissa strengthens into a dangerous Category 4 storm, threatening massive flooding and damage.",
    "content": """
      A major weather alert is in effect for the Caribbean as Hurricane Melissa has rapidly intensified into a dangerous Category 4 storm. The hurricane is on a direct path toward Jamaica and Haiti, which are now bracing for a potentially catastrophic impact.
      
      Forecasters warn of devastating winds and a massive storm surge, with "catastrophic" flooding expected. Authorities in Jamaica have begun shutting down key airports and are urging residents in low-lying areas to evacuate immediately. The storm is forecast to possibly strengthen even further as it approaches land.
    """
  },
  {
    "slug": "russia-tests-burevestnik-nuclear-missile",
    "image": "missile.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Russia Tests 'Invincible' Nuclear-Powered Missile",
    "excerpt": "President Putin announced the successful test of the 'Burevestnik' nuclear-powered cruise missile, a weapon he claims can bypass all existing defense systems.",
    "content": """
      Russia has announced a significant and alarming escalation in its strategic weapons program. President Vladimir Putin confirmed the successful completion of decisive tests for the "Burevestnik" nuclear-powered cruise missile.
      
      This weapon, which officials have dubbed "invincible," reportedly has a range of over 8,700 miles (14,000 km) and is specifically designed to bypass all existing and future air defense systems. The test signals a major technological claim and is raising alarms in Western capitals about a new arms race and a threat to global strategic stability.
    """
  },
  {
    "slug": "javier-milei-wins-argentina-election",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Milei Claims Victory in Key Argentina Election",
    "excerpt": "Argentina's President Javier Milei has declared victory in a high-stakes election, seen as a crucial public referendum on his radical economic 'shock therapy' policies.",
    "content": """
      Argentina's President Javier Milei has claimed victory in the country's high-stakes (midterm) elections. The results are being widely interpreted as a crucial, hard-won referendum on his radical austerity measures and "shock therapy" economic policies, which are aimed at slowing hyperinflation.
      
      The win could provide his government with a new mandate to continue its reforms, despite the massive budget cuts. In a notable reaction, US President Donald Trump congratulated Milei, stating that the Argentine leader "had a lot of help from the US" to secure the victory.
    """
  },
  {
    "slug": "louvre-heist-suspects-arrested",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Breakthrough in $100M Louvre Jewel Heist",
    "excerpt": "French police have arrested two suspects in connection with the audacious $100 million theft of crown jewels from the Louvre museum in Paris.",
    "content": """
      French police have made a major breakthrough in the sensational $100 million Louvre jewel heist. Authorities confirmed the arrest of two suspects in connection with the daring theft of crown jewels that captured global attention and sparked a massive manhunt.
      
      One of the suspects was reportedly apprehended at a Paris airport while attempting to board a flight to Algeria. While the arrests are a significant step, the priceless jewels have not yet been recovered. The investigation continues as authorities search for the stolen items and any other potential accomplices.
    """
  },
  {
    "slug": "asean-summit-welcomes-timor-leste",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "ASEAN Welcomes Timor-Leste as 11th Member",
    "excerpt": "In a historic move, the ASEAN summit officially welcomed Timor-Leste as its 11th full member. The summit is also addressing regional security and trade.",
    "content": """
      Today marks a historic day at the 47th ASEAN Summit in Malaysia, as Timor-Leste was officially welcomed as the bloc's 11th full member. Leaders, including Philippine President Marcos Jr., hailed the admission as a powerful demonstration of ASEAN's commitment to regional unity and cooperation.
      
      The summit, also attended by US President Trump, is focused on key regional issues. This includes the successful de-escalation of border tensions between Cambodia and Thailand, who have reportedly begun removing heavy military assets from disputed areas following a pact.
    """
  },
  {
    "slug": "middle-east-ceasefire-talks-gaza",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "China Calls for 'Lasting Ceasefire' in Gaza",
    "excerpt": "China's Foreign Minister called for a 'genuine and lasting ceasefire' and a two-state solution, as humanitarian teams are reportedly granted access to Gaza.",
    "content": """
      Amid ongoing volatility in the Middle East, China’s Foreign Minister today called for a "genuine, comprehensive, and lasting ceasefire" in Gaza. In a major policy speech, he also reiterated China's push for the full implementation of the two-state solution to ensure lasting stability.
      
      This diplomatic push comes as the Red Cross and Egyptian teams have reportedly been granted access to Gaza to begin the grim task of searching for the bodies of Israeli hostages. Meanwhile, a US aide stated a recent Israeli strike on a militant was not a ceasefire violation.
    """
  },
  {
    "slug": "unrest-mali-cameroon-protests",
    "image": "cranes.jpg",
    "author": "Global News Desk",
    "date": date(2025,10,27),
    "title": "Instability Flares in Mali and Cameroon",
    "excerpt": "Mali is facing a crippling fuel blockade that has shut down schools, while in Cameroon, at least four have died in post-election protests.",
    "content": """
      Instability is flaring in parts of Africa today. In Mali, the government has been forced to shut down schools across the country as a crippling fuel blockade, imposed by various fighter groups, continues to paralyse daily life and essential services.
      
      Meanwhile, violent tensions have erupted in Cameroon following the presidential election. At least four protesters have reportedly been killed in clashes with security forces after the long-time incumbent, Paul Biya, was declared the winner. The opposition has rejected the results, claiming victory for themselves and sparking fears of further violence.
    """
  }
]

def get_title(post:dir):
    return post['title']


# Create your views here.
def start_page(request):
    sorted_posts = sorted(all_posts,key=get_title)
    latest_posts = sorted_posts[-4:]
    return render(request,"blog/index.html", {"posts": latest_posts})


def list_posts(request):
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def detail_post(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post":identified_post})