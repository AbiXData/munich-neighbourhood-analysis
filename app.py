import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Page config
st.set_page_config(
    page_title="Munich District Finder",
    page_icon="🏙️",
    layout="wide"
)

# Data
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'district_id': list(range(1, 26)),
        'district_name': [
            'Altstadt-Lehel', 'Maxvorstadt', 'Schwabing-West', 'Schwabing-Freimann',
            'Au-Haidhausen', 'Sendling', 'Sendling-Westpark', 'Schwanthalerhöhe',
            'Neuhausen-Nymphenburg', 'Moosach', 'Milbertshofen-Am Hart',
            'Bogenhausen', 'Berg am Laim', 'Trudering-Riem', 'Ramersdorf-Perlach',
            'Obergiesing-Fasangarten', 'Untergiesing-Harlaching',
            'Thalkirchen-Obersendling-Forstenried', 'Hadern',
            'Pasing-Obermenzing', 'Aubing-Lochhausen-Langwied',
            'Allach-Untermenzing', 'Feldmoching-Hasenbergl', 'Laim', 'Maxvorstadt-West'
        ],
        'unemployment_rate': [4.2,3.8,3.5,3.2,4.8,5.2,4.6,5.8,3.4,5.6,6.2,2.8,5.9,4.8,6.4,5.1,3.9,3.6,4.1,3.7,5.3,4.2,7.1,5.4,3.9],
        'crime_rate': [98.2,42.1,35.4,28.6,52.3,38.7,31.2,45.6,29.8,41.3,48.7,22.4,43.2,35.6,51.8,38.4,27.9,25.3,28.7,26.4,32.1,24.8,55.3,40.2,33.6],
        'avg_rent_eur': [2100,1950,1850,1750,1800,1550,1500,1650,1900,1450,1400,2050,1350,1300,1380,1420,1600,1680,1550,1480,1250,1200,1180,1420,1750],
        'latitude': [48.1372,48.1508,48.1588,48.1750,48.1272,48.1172,48.1222,48.1322,48.1572,48.1750,48.1850,48.1472,48.1272,48.1222,48.1072,48.1022,48.0922,48.0822,48.1072,48.1422,48.1372,48.1572,48.1950,48.1422,48.1372],
        'longitude': [11.5755,11.5655,11.5555,11.6055,11.6055,11.5455,11.5055,11.5355,11.5155,11.5055,11.5655,11.6255,11.6355,11.6755,11.6155,11.5855,11.5655,11.5255,11.4955,11.4655,11.4355,11.4355,11.5155,11.5155,11.4955]
    })

    features = ['unemployment_rate', 'crime_rate', 'avg_rent_eur']
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data[features])
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    data['cluster'] = kmeans.fit_predict(scaled)
    label_map = {0: 'Least Desirable', 1: 'Desirable', 2: 'Semi-Desirable', 3: 'Most Desirable'}
    data['desirability'] = data['cluster'].map(label_map)
    return data

df = load_data()

# Header
st.title("🏙️ Munich District Finder for New Immigrants")
st.markdown("**By Abi Tijani | Data Analyst | Munich, Germany | 2026**")
st.markdown("*Use this tool to find the best Munich district based on your priorities.*")
st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Set Your Priorities")
st.sidebar.markdown("Adjust the filters to find your ideal Munich district.")

max_rent = st.sidebar.slider(
    "Maximum Monthly Rent (EUR)",
    min_value=1000,
    max_value=2200,
    value=1800,
    step=50,
    help="Set your maximum budget for a 1-bedroom apartment"
)

max_crime = st.sidebar.slider(
    "Maximum Crime Rate (per 1,000 residents)",
    min_value=20,
    max_value=100,
    value=55,
    step=5,
    help="Lower is safer. Munich average is 38.4"
)

max_unemployment = st.sidebar.slider(
    "Maximum Unemployment Rate (%)",
    min_value=2.0,
    max_value=8.0,
    value=6.0,
    step=0.5,
    help="Lower means more job opportunities nearby"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Data Sources:**")
st.sidebar.markdown("- Munich Crime Atlas 2023")
st.sidebar.markdown("- Statistisches Amt München 2023")
st.sidebar.markdown("- Immoscout24 2024")
st.sidebar.markdown("---")
st.sidebar.markdown("**Links:**")
st.sidebar.markdown("[GitHub Repo](https://github.com/AbiXData/munich-neighbourhood-analysis)")
st.sidebar.markdown("[Medium Article](https://medium.com/@abixdata/analysis-of-munich-neighbourhoods-for-new-immigrants-using-machine-learning-23a732b05981)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/abitijani/)")

# Filter data
filtered = df[
    (df['avg_rent_eur'] <= max_rent) &
    (df['crime_rate'] <= max_crime) &
    (df['unemployment_rate'] <= max_unemployment)
].copy()

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Districts Found", len(filtered), f"out of {len(df)}")
col2.metric("Avg Rent", f"EUR {filtered['avg_rent_eur'].mean():.0f}" if len(filtered) > 0 else "N/A")
col3.metric("Avg Crime Rate", f"{filtered['crime_rate'].mean():.1f}" if len(filtered) > 0 else "N/A")
col4.metric("Avg Unemployment", f"{filtered['unemployment_rate'].mean():.1f}%" if len(filtered) > 0 else "N/A")

st.markdown("---")

if len(filtered) == 0:
    st.warning("No districts match your filters. Try adjusting the sliders.")
else:
    # Top recommendations
    st.subheader("🏆 Top Recommended Districts for You")
    top3 = filtered.sort_values(['crime_rate', 'unemployment_rate', 'avg_rent_eur']).head(3)

    rec_cols = st.columns(3)
    medals = ["🥇", "🥈", "🥉"]
    for i, (_, row) in enumerate(top3.iterrows()):
        with rec_cols[i]:
            st.markdown(f"### {medals[i]} {row['district_name']}")
            st.markdown(f"**Desirability:** {row['desirability']}")
            st.markdown(f"**Rent:** EUR {row['avg_rent_eur']:,}/month")
            st.markdown(f"**Crime Rate:** {row['crime_rate']} per 1,000")
            st.markdown(f"**Unemployment:** {row['unemployment_rate']}%")

    st.markdown("---")

    # Two columns layout
    left, right = st.columns(2)

    with left:
        st.subheader("🗺️ District Map")
        color_map = {
            'Most Desirable': '#2ecc71',
            'Desirable': '#f1c40f',
            'Semi-Desirable': '#e67e22',
            'Least Desirable': '#e74c3c'
        }
        fig_map = px.scatter_mapbox(
            filtered,
            lat='latitude', lon='longitude',
            color='desirability',
            size='avg_rent_eur',
            hover_name='district_name',
            hover_data={'unemployment_rate': True, 'crime_rate': True, 'avg_rent_eur': True, 'latitude': False, 'longitude': False},
            color_discrete_map=color_map,
            zoom=10,
            center={'lat': 48.1372, 'lon': 11.5755},
            height=420
        )
        fig_map.update_layout(mapbox_style='open-street-map', margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)

    with right:
        st.subheader("📊 Desirability Index")
        plot_df = filtered.sort_values(['desirability', 'crime_rate'])
        fig_bar = px.bar(
            plot_df,
            x='crime_rate', y='district_name',
            orientation='h',
            color='desirability',
            color_discrete_map=color_map,
            labels={'crime_rate': 'Crime Rate (per 1,000)', 'district_name': 'District'},
            height=420
        )
        fig_bar.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # Full data table
    st.subheader("📋 All Matching Districts")
    display_df = filtered[['district_name', 'desirability', 'avg_rent_eur', 'crime_rate', 'unemployment_rate']].sort_values('crime_rate')
    display_df.columns = ['District', 'Desirability', 'Avg Rent (EUR)', 'Crime Rate', 'Unemployment (%)']
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    # Bubble chart
    st.markdown("---")
    st.subheader("🔵 Crime vs Unemployment (bubble size = rent)")
    fig_bubble = px.scatter(
        filtered,
        x='unemployment_rate', y='crime_rate',
        size='avg_rent_eur',
        color='desirability',
        hover_name='district_name',
        color_discrete_map=color_map,
        labels={'unemployment_rate': 'Unemployment Rate (%)', 'crime_rate': 'Crime Rate (per 1,000)'},
        height=400
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

st.markdown("---")
st.markdown("Built by **Abi Tijani** | Data Analyst | Munich, Germany | 2026")
st.markdown("[GitHub](https://github.com/AbiXData/munich-neighbourhood-analysis) | [Medium](https://medium.com/@abixdata/analysis-of-munich-neighbourhoods-for-new-immigrants-using-machine-learning-23a732b05981) | [LinkedIn](https://www.linkedin.com/in/abitijani/)")
