from datetime import date

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from constants import *
from dashboard import *
from helpers import get_data_dict, show_projects

# Set page title
st.set_page_config(
    page_title="Researcher Profile and STEM Data Explorer", layout="wide"
)

# Constants
# df = pd.read_csv("st_assignment.csv",index_col=0).drop(columns=['Unnamed: 0'])

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Student Profile", "Projects", "Some Music", "Contact"],
)


# Sections based on menu selection
if menu == "Student Profile":
    with st.container():
        st.title("❯ whoami", text_alignment="center")
        col1, col2 = st.columns(2)

        st.sidebar.header("Profile Options", text_alignment="center")

        with col1.container():
            st.image(
                "assets/profile_pic.png",
                caption="This is what I look like btw",
                width="content",
            )
        with col2.container():
            st.markdown(DETAILS)

        st.divider()

    col3, col4 = st.columns(2)
    with col3.container():
        st.subheader("About Me")
        st.write(ABOUT_ME)

        st.divider()

        st.subheader("Publications")
        st.write(PUBLICATIONS)
    with col4.container():
        st.subheader("What I use")
        st.write(TECH_STACK)


elif menu == "Projects":
    st.title("Projects", text_alignment="center")

    st.html(show_projects().as_raw_html())

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Audio Feature Pipeline")
            st.markdown(Proj_AFP)

        with col2:
            st.write("Bayesian Network")
            st.markdown(Proj_BN)

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Tutorial Automation")
            st.markdown(Proj_QE)

        with col2:
            st.write("Churn Prediction")
            st.markdown(Proj_CP)

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Chess")
            st.markdown(Proj_Chess)

        with col2:
            st.write("Anomaly Detection")
            st.markdown(Proj_AD)


elif menu == "Some Music":

    options = st.sidebar.selectbox(label="Preview Option", options=["Raw", "Dashboard"])

    if options == "Raw":
        st.title("My own music listening history", text_alignment="center")
        st.write("The audio feature pipeline ain't done yet but I can show you this")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Number of Observations(n)", value=len(df), border=True)
        with col2:
            perc = 1 - len(df.dropna()) / len(df)
            st.metric(label="N/A (as percentage)", value=f"{perc*100}%", border=True)
        with col3:
            uniques = df[["Artist", "TrackName"]].nunique()
            st.metric(
                label="Unique Observations(Artist | Track)",
                value=f"A:{uniques.loc['Artist']}| T:{uniques.loc['TrackName']}",
                border=True,
            )
        st.dataframe(df)

        st.divider()

        st.html(get_data_dict().as_raw_html())

    if options == "Dashboard":

        st.title("Dashboard")

        start_yr, end_yr = st.sidebar.slider(
            "Select years", min_value=2019, max_value=2025, value=(2019, 2025)
        )
        start_month,end_month = st.sidebar.slider(label='Select Months',min_value=1,max_value=12,value=(1,12))
        top_n_artists = st.sidebar.number_input(
            "Select top n artists", min_value=3, max_value=50, value=5
        )

        sub = subset(start_yr, end_yr,start_month,end_month)

        selected_artist = st.sidebar.selectbox(
            "Select an artist", top_artists(sub, top_n_artists)
        )

        with st.container():
            col1, col2 = st.columns(2)

            with col1:

                plot = px.line(
                    groupby_date(sub),
                    x="date",
                    y="TrackName",
                    title="Number of Songs Listened",
                )
                st.plotly_chart(plot)
            with col2:
                col3, col4 = st.columns(2)
                with col3:
                    artist = most_impactful_artist_by_af(sub)
                    st.subheader("Artist")
                    st.metric("Most Emotional", artist["valence"])
                    st.metric("Most Energetic", artist["energy"])
                    st.metric("Speechiest", artist["speechiness"])
                    st.metric("Most Acoustic", artist["acousticness"])
                with col4:
                    song = most_impactful_song_by_af(sub)
                    st.subheader("Track")
                    st.metric("Most Emotional", song["valence"])
                    st.metric("Most Energetic", song["energy"])
                    st.metric("Speechiest", song["speechiness"])
                    st.metric("Most Acoustic", song["acousticness"])

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                pop = px.line(
                    groupby_date(sub),
                    x="date",
                    y="Artist",
                    title="Number of Artists Listened",
                )
                st.plotly_chart(pop)

            with col2:
                artist = artist_grouped(sub, selected_artist).sort_values(by="listened")

                plot = px.bar(
                    data_frame=artist,
                    x="listened",
                    y="TrackName",
                    title=f"Top songs by {selected_artist}",
                    orientation="h",
                )
                st.plotly_chart(plot)

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                artists = (
                    top_n(sub, top_n_artists)
                    .groupby("Artist",as_index=False)["TrackName"]
                    .count()
                    .sort_values(ascending=True,by='TrackName')
                )

                # st.dataframe(artists)
                plot = px.bar(
                    data_frame=artists,
                    x="TrackName",
                    y="Artist",
                    orientation="h",
                    title=f"Top {top_n_artists} artists from {start_yr} to {end_yr}",
                )
                st.plotly_chart(plot)

            with col2:
                minutes = round(sub['ms_played'].sum() / 3600000 ,2)
                total_tracks = sub['TrackName'].count()
                total_artists = len(sub['Artist'].unique())
                
                st.metric('Total Hours played', f'{minutes} hours')
                st.metric('Total Tracks played', f'{total_tracks} tracks')
                st.metric("Total Artists played", f'{total_artists} artists')


elif menu == "Contact":
    st.title("Contact Information",text_alignment='center')

    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.Vn8Aa5ypdPND2xyceZIAdAHaHS%3Fpid%3DApi&f=1&ipt=defb3995916e664f485363b6477bba5f77122a861cfdbc529e99bed2f182850f&ipo=images",width=50)
    st.markdown('[AlexTabble](https://github.com/AlexTabble)')

    st.divider()

    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%2Fid%2FOIP.Fc-evvSo3ccnVv1tjSvkcQHaHa%3Fpid%3DApi&f=1&ipt=b70ae9d709ded97d65d02150d116b4640efc37239a383da8ee5e94e682cc39cc&ipo=images",width=50)
    st.markdown("[Alexander Leak](https://www.linkedin.com/in/alexander-leak12/)")

    st.divider()

    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.eNhNUxYKONbzDq9WELfu7wHaE8%3Fpid%3DApi&f=1&ipt=c0d03bb1763c4024920384f5bc75f1ce7b6599afc6ea4535e0eeb030284b3161&ipo=images",width=50)

    st.text('alexanderjleak@gmail.com')


