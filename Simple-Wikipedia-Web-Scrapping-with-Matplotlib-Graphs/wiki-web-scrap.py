#-----------------------------------------------------------------------
#-- Simple Web Scraping with Data Visualisations in Matplotlib module
#-----------------------------------------------------------------------

website_to_parse = "http://leagueoflegends.wikia.com/wiki/Base_champion_statistics"

# Saves HTML to soup object
html_data = requests.get(website_base_stats).text
soup = BeautifulSoup(html_data, "html5lib")

# Parse table and save to pandas data frame
table = soup.find('table', attrs={'class' : 'wikitable'})
table_body = table.tbody

data = []
rows = table_body.find_all('td')
for row in rows:
     
     # Retrieve table data from each rows
     cols = row.find_all('td')
     if len(cols) == 0:
         continue
     cols[0] = cols[0].span
     
     # Strips out the text content from the column
     cols = [c.text.strip() for c in cols]
     
     # Appends the stripped text onto a named "data" list
     data.append(cols)

lol_thead = [h.text.strip() for h in soup.find_all("th")]
lol_table = pd.DataFrame(data, columns=lol_thead)

''' Produces on screen visualisation using Matplotlib methods '''
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.title.set_text('Plot 1')
ax1.scatter(x=lol_table.HP, y=lol_table.Range)    # generic scatter plot with no extra customisations

''' Plot 2 '''
ax2.title.set_text('Plot 2')
ax2 = fig.add_subplot(222)
ax2.scatter(x=lol_table.HP, y=lol_table.Range)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False) 
ax2.set(xlabel = "HP", ylabel ="Range")   # set x and y labelled axis


''' Plot 3: sets vertical lines, customised with axvlines 
    x-axis breaks and labels were set with xaxis.set   '''

ax3 = fig.add_subplot(223)
ax3.title.set_title('Plot 3')
ax3.scatter(x=lol_table.HP, y=lol_table.Range)

for vline in range(300, 700, 100):
    ax3.axvline(vline, color="grey", linestyle="dashed", linewidth=0.5)

axis.xaxis.set(
        tick=range(300, 700, 100)
        ticklabels=["HP: {}".format(x) for x in range(300, 700, 50)]
)

''' Plot 4: marker type and colour on the scatter plot were specified
    x and y limits were set with the addition of a text added to the plot '''
ax4 = fig.add_subplot(224)
ax4 = fig.add_subplot(224)
ax4 = fig.add_subplot(224)
ax4.title.set_text("Plot 4")
ax4.scatter(x=lol_table.HP, y=lol_table.Range, markers="+", color="red")

ax4.set(
    xlim=[450, 650]
    ylim=[400,700] )

ax4.text(600, 550, "Zoom!", style="italic", fontsize="x-large")
