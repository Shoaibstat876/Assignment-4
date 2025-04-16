import streamlit as st
import requests

st.set_page_config(page_title="Country Information Cards", layout="wide")

# --- Title ---
st.title("🌍 Country Information Cards")
st.markdown("Get quick facts and stats about any country with just one click!")

# --- Helper Function ---
@st.cache_data
def get_country_data(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    info = {
        "Country": data.get("name", {}).get("common", "N/A"),
        "Capital": data.get("capital", ["N/A"])[0],
        "Region": data.get("region", "N/A"),
        "Subregion": data.get("subregion", "N/A"),
        "Population": f"{data.get('population', 0):,}",
        "Area (km²)": f"{data.get('area', 0):,}",
        "Currency": ", ".join([v["name"] for v in data.get("currencies", {}).values()]),
        "Language(s)": ", ".join(data.get("languages", {}).values()),
        "Flag": data.get("flags", {}).get("png", ""),
        "Map": data.get("maps", {}).get("googleMaps", ""),
    }
    return info

# --- Input ---
country = st.text_input("Enter a country name (e.g., Japan, Pakistan, France)", "")

# --- Output ---
if country:
    data = get_country_data(country.strip())

    if data:
        st.image(data["Flag"], width=150)
        st.subheader(data["Country"])
        st.write(f"**Capital**: {data['Capital']}")
        st.write(f"**Region**: {data['Region']} → {data['Subregion']}")
        st.write(f"**Population**: {data['Population']}")
        st.write(f"**Area**: {data['Area (km²)']} km²")
        st.write(f"**Currency**: {data['Currency']}")
        st.write(f"**Language(s)**: {data['Language(s)']}")
        st.markdown(f"[🌐 View on Google Maps]({data['Map']})")
    else:
        st.error("Country not found! Please try a different name.")

st.markdown("---")
st.caption("Made with 💖 using Python & Streamlit")
