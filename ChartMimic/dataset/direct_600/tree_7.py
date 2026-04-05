
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [25.00, 20.00, 15.00, 13.00, 10.00, 8.00, 5.00, 4.00]
labels = [
    "Facebook\n25.00%",
    "YouTube\n20.00%",
    "WhatsApp\n15.00%",
    "Instagram\n13.00%",
    "TikTok\n10.00%",
    "Snapchat\n8.00%",
    "Twitter\n5.00%",
    "LinkedIn\n4.00%",
]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = [
    "#66c2a5", # Facebook
    "#fc8d62", # YouTube
    "#8da0cb", # WhatsApp
    "#e78ac3", # Instagram
    "#a6d854", # TikTok
    "#ffd92f", # Snapchat
    "#e5c494", # Twitter
    "#b3b3b3", # LinkedIn
]
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={"fontsize": 18}
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_7.pdf', bbox_inches='tight')

