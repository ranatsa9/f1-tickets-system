import streamlit as st

# =========================
# Page Setup
# =========================

st.set_page_config(
    page_title="F1 Ticket Reservation System",
    page_icon="🏎️",
    layout="wide"
)

# =========================
# Person 1: Race Database
# =========================

races = {
    "Spanish Grand Prix": {
        "Round": 9,
        "Country": "Spain",
        "Flag": "🇪🇸",
        "Price": 400,
        "Location": "Circuit de Barcelona-Catalunya",
        "Time": "16:00",
        "Date": "2026-06-14",
        "Display Date": "12 - 14 Jun",
        "Status": "Completed"
    },
    "Austrian Grand Prix": {
        "Round": 10,
        "Country": "Austria",
        "Flag": "🇦🇹",
        "Price": 550,
        "Location": "Red Bull Ring, Spielberg",
        "Time": "16:00",
        "Date": "2026-06-28",
        "Display Date": "26 - 28 Jun",
        "Status": "Full"
    },
    "British Grand Prix": {
        "Round": 11,
        "Country": "Great Britain",
        "Flag": "🇬🇧",
        "Price": 750,
        "Location": "Silverstone Circuit",
        "Time": "17:00",
        "Date": "2026-07-05",
        "Display Date": "03 - 05 Jul",
        "Status": "Available"
    },
    "Belgian Grand Prix": {
        "Round": 12,
        "Country": "Belgium",
        "Flag": "🇧🇪",
        "Price": 620,
        "Location": "Circuit de Spa-Francorchamps",
        "Time": "16:00",
        "Date": "2026-07-19",
        "Display Date": "17 - 19 Jul",
        "Status": "Full"
    },
    "Hungarian Grand Prix": {
        "Round": 13,
        "Country": "Hungary",
        "Flag": "🇭🇺",
        "Price": 480,
        "Location": "Hungaroring, Budapest",
        "Time": "16:00",
        "Date": "2026-07-26",
        "Display Date": "24 - 26 Jul",
        "Status": "Available"
    },
    "Dutch Grand Prix": {
        "Round": 14,
        "Country": "Netherlands",
        "Flag": "🇳🇱",
        "Price": 580,
        "Location": "Circuit Zandvoort",
        "Time": "16:00",
        "Date": "2026-08-23",
        "Display Date": "21 - 23 Aug",
        "Status": "Available"
    },
    "Italian Grand Prix": {
        "Round": 15,
        "Country": "Italy",
        "Flag": "🇮🇹",
        "Price": 650,
        "Location": "Autodromo Nazionale Monza",
        "Time": "16:00",
        "Date": "2026-09-06",
        "Display Date": "04 - 06 Sep",
        "Status": "Available"
    },
    "Spanish Grand Prix - Madrid": {
        "Round": 16,
        "Country": "Spain",
        "Flag": "🇪🇸",
        "Price": 695,
        "Location": "Madrid Circuit",
        "Time": "16:00",
        "Date": "2026-09-13",
        "Display Date": "11 - 13 Sep",
        "Status": "Available"
    },
    "Azerbaijan Grand Prix": {
        "Round": 17,
        "Country": "Azerbaijan",
        "Flag": "🇦🇿",
        "Price": 450,
        "Location": "Baku City Circuit",
        "Time": "14:00",
        "Date": "2026-09-27",
        "Display Date": "25 - 27 Sep",
        "Status": "Available"
    },
    "Singapore Grand Prix": {
        "Round": 18,
        "Country": "Singapore",
        "Flag": "🇸🇬",
        "Price": 800,
        "Location": "Marina Bay Street Circuit",
        "Time": "15:00",
        "Date": "2026-10-11",
        "Display Date": "09 - 11 Oct",
        "Status": "Full"
    },
    "United States Grand Prix": {
        "Round": 19,
        "Country": "United States",
        "Flag": "🇺🇸",
        "Price": 700,
        "Location": "Circuit of The Americas, Austin",
        "Time": "23:00",
        "Date": "2026-10-25",
        "Display Date": "23 - 25 Oct",
        "Status": "Available"
    },
    "Mexican Grand Prix": {
        "Round": 20,
        "Country": "Mexico",
        "Flag": "🇲🇽",
        "Price": 500,
        "Location": "Autódromo Hermanos Rodríguez",
        "Time": "23:00",
        "Date": "2026-11-01",
        "Display Date": "30 Oct - 01 Nov",
        "Status": "Available"
    },
    "Brazilian Grand Prix": {
        "Round": 21,
        "Country": "Brazil",
        "Flag": "🇧🇷",
        "Price": 600,
        "Location": "Interlagos, São Paulo",
        "Time": "20:00",
        "Date": "2026-11-08",
        "Display Date": "06 - 08 Nov",
        "Status": "Available"
    },
    "Las Vegas Grand Prix": {
        "Round": 22,
        "Country": "Las Vegas",
        "Flag": "🇺🇸",
        "Price": 900,
        "Location": "Las Vegas Strip Circuit",
        "Time": "06:00",
        "Date": "2026-11-21",
        "Display Date": "19 - 21 Nov",
        "Status": "Available"
    },
    "Qatar Grand Prix": {
        "Round": 23,
        "Country": "Qatar",
        "Flag": "🇶🇦",
        "Price": 700,
        "Location": "Lusail International Circuit",
        "Time": "19:00",
        "Date": "2026-11-29",
        "Display Date": "27 - 29 Nov",
        "Status": "Available"
    },
    "Abu Dhabi Grand Prix": {
        "Round": 24,
        "Country": "Abu Dhabi",
        "Flag": "🇦🇪",
        "Price": 850,
        "Location": "Yas Marina Circuit",
        "Time": "17:00",
        "Date": "2026-12-06",
        "Display Date": "04 - 06 Dec",
        "Status": "Available"
    }
}

# =========================
# CSS Styling
# =========================

st.markdown("""
<style>
.stApp {
    background-color: #070b14;
    color: white;
}

.f1-header {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 25px;
    border: 1px solid #2d3748;
    box-shadow: 0 8px 18px rgba(0,0,0,0.35);
}

.f1-main-title {
    font-size: 42px;
    font-weight: 900;
    color: white;
    margin-bottom: 5px;
}

.f1-subtitle {
    color: #d1d5db;
    font-size: 18px;
}

.f1-card {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 10px;
    min-height: 335px;
    border: 1px solid #374151;
    box-shadow: 0 4px 12px rgba(0,0,0,0.35);
}

.f1-round {
    color: #9ca3af;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 1px;
}

.f1-country {
    color: white;
    font-size: 28px;
    font-weight: 900;
    margin-top: 5px;
}

.f1-race-name {
    color: #d1d5db;
    font-size: 13px;
    text-transform: uppercase;
    margin-top: 4px;
    min-height: 35px;
}

.f1-date {
    color: #60a5fa;
    font-size: 25px;
    font-weight: bold;
    margin-top: 14px;
}

.f1-info {
    color: #e5e7eb;
    font-size: 14px;
    margin-top: 7px;
}

.available {
    color: #22c55e;
    font-weight: bold;
}

.full {
    color: #ef4444;
    font-weight: bold;
}

.completed {
    color: #9ca3af;
    font-weight: bold;
}

.payment-box {
    background: linear-gradient(135deg, #111827, #0f172a);
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #334155;
    margin-top: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.35);
    color: white;
}

.receipt-box {
    background: linear-gradient(135deg, #101827, #172033);
    padding: 28px;
    border-radius: 22px;
    border: 1px solid #475569;
    margin-top: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.45);
}

.receipt-title {
    color: white;
    font-size: 28px;
    font-weight: 900;
    margin-bottom: 5px;
}

.receipt-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 20px;
}

.receipt-row {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #334155;
    padding: 10px 0;
    color: #e5e7eb;
    font-size: 15px;
}

.receipt-label {
    color: #94a3b8;
    font-weight: 600;
}

.receipt-value {
    color: white;
    font-weight: 700;
    text-align: right;
}

.receipt-total {
    background-color: #dc2626;
    color: white;
    padding: 15px;
    border-radius: 14px;
    margin-top: 18px;
    font-size: 20px;
    font-weight: 900;
    text-align: center;
}

.confirmed-badge {
    background-color: #16a34a;
    color: white;
    padding: 8px 14px;
    border-radius: 999px;
    font-weight: 800;
    display: inline-block;
    margin-top: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Person 3: Functions
# =========================

def calculate_total(cart_item, database):
    subtotal = 0
    race_name = cart_item["Race"]
    quantity = cart_item["Quantity"]

    if race_name in database:
        unit_price = database[race_name]["Price"]
        subtotal = unit_price * quantity

    return subtotal


apply_discount = lambda amount: amount * 0.85
apply_tax = lambda amount: amount * 1.15

# =========================
# Main Header
# =========================

st.markdown("""
<div class="f1-header">
    <div class="f1-main-title">🏎️ F1 Ticket Reservation System</div>
    <div class="f1-subtitle">Browse Grand Prix events, check ticket availability, and reserve your seats.</div>
</div>
""", unsafe_allow_html=True)

# =========================
# Person 1: Search Feature
# =========================

st.write("## Search for a Race")
search_feature = st.text_input("Enter race name, for example: British, Qatar, or Abu Dhabi").lower()

st.write("## 2026 Formula 1 Race Schedule")

# =========================
# Person 1 + Person 2: Race Cards - Two per row
# =========================

filtered_races = []

for race_name, details in races.items():
    if search_feature and search_feature not in race_name.lower() and search_feature not in details["Country"].lower():
        continue

    filtered_races.append((race_name, details))

if len(filtered_races) == 0:
    st.warning("No race found. Try searching with another race name.")

else:
    for i in range(0, len(filtered_races), 2):

        col1, col2 = st.columns(2)
        row_races = filtered_races[i:i + 2]

        for col, race_data in zip([col1, col2], row_races):

            race_name = race_data[0]
            details = race_data[1]

            with col:
                status = details["Status"]

                if status == "Available":
                    status_class = "available"
                    status_text = "AVAILABLE TO BOOK"
                elif status == "Full":
                    status_class = "full"
                    status_text = "SOLD OUT"
                else:
                    status_class = "completed"
                    status_text = "COMPLETED"

                st.markdown(f"""
                <div class="f1-card">
                    <div class="f1-round">{details['Flag']} ROUND {details['Round']}</div>
                    <div class="f1-country">{details['Country']}</div>
                    <div class="f1-race-name">Formula 1 {race_name} 2026</div>
                    <div class="f1-date">{details['Display Date']}</div>
                    <div class="f1-info">📍 {details['Location']}</div>
                    <div class="f1-info">⏰ {details['Time']}</div>
                    <div class="f1-info">💰 {details['Price']} SAR</div>
                    <div class="f1-info">Status: <span class="{status_class}">{status_text}</span></div>
                </div>
                """, unsafe_allow_html=True)

                if details["Status"] == "Available":
                    if st.button("🎟️ Reserve This Race", key=f"reserve_{race_name}"):
                        st.session_state["selected_race"] = race_name
                        st.session_state["selected_details"] = details

                elif details["Status"] == "Full":
                    st.warning("This race is sold out.")

                elif details["Status"] == "Completed":
                    st.info("Booking is closed.")

# =========================
# Person 2: Reservation Form
# =========================

if "selected_race" in st.session_state:

    selected_race = st.session_state["selected_race"]
    selected_details = st.session_state["selected_details"]

    st.write("---")
    st.write("## Complete Your Reservation")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"🏁 **Selected Race:** {selected_race}")
        st.write(f"📍 **Location:** {selected_details['Location']}")
        st.write(f"📅 **Date:** {selected_details['Date']}")
        st.write(f"⏰ **Time:** {selected_details['Time']}")

    with col2:
        st.write(f"💰 **Price per Ticket:** {selected_details['Price']} SAR")
        st.write(f"🎟️ **Status:** {selected_details['Status']}")

    ticket_quantity = st.number_input(
        "How many tickets would you like to reserve?",
        min_value=1,
        max_value=10,
        value=1
    )

    booking_user = {
        "Race": selected_race,
        "Location": selected_details["Location"],
        "Date": selected_details["Date"],
        "Time": selected_details["Time"],
        "Price": selected_details["Price"],
        "Quantity": ticket_quantity,
        "Status": selected_details["Status"]
    }

    st.success("Your booking selection has been saved.")

    # =========================
    # Person 3: Calculations & Discounts
    # =========================
def calculate_total(cart_item, database): 

    subtotal = 0 

    race_name = cart_item["Race"]

    quantity = cart_item["Quantity"]

    

    if race_name in database: 

        unit_price = database[race_name]['Price']

        subtotal = unit_price * quantity 

    return subtotal



# Lambda functions for financial calculations

apply_discount = lambda amount: amount * 0.85  # 15% discount

apply_tax = lambda amount: amount * 1.15       # 15% VAT



# Define the valid discount codes

VALID_MEMBERSHIP_CODES = ["F1CLUB2026", "POLEPOSITION", "VIPPASS"]



# Only execute if a race has been selected

if "selected_race" in st.session_state:

    

    st.write("---")

    st.write("### 🔐 Membership Authentication")

    

    # Text input for authenticating membership instead of a simple checkbox

    user_code = st.text_input(

        "Enter your 10-digit F1 Club Membership ID or Promo Code:", 

        placeholder="e.g., F1CLUB2026"

    ).strip()



    # 1. Calculate the base subtotal

    order_subtotal = calculate_total(booking_user, races)



# 2. Authenticate code and apply discount conditionally

    is_authenticated = False



if user_code:  # If the user typed something

        if user_code in VALID_MEMBERSHIP_CODES:

            discounted_total = apply_discount(order_subtotal)

            is_authenticated = True

            st.success(" Membership authenticated! 15% VIP discount applied.")

        else:

            discounted_total = order_subtotal

            st.error("Invalid Code. Please check your credentials or continue without a discount.")

else:

        discounted_total = order_subtotal  # No code entered       



# 3. Apply VAT to the final running total

final_total_with_tax = apply_tax(discounted_total)

# 4. Output the final payment breakdown to the UI

st.write("### 💳 Final Payment Details")

    

col_billing1, col_billing2 = st.columns(2)

with col_billing1:

        st.write(f"**Base Subtotal:**")

        if is_authenticated:

            st.write(f"**Discounted Subtotal:**")

        st.write(f"**Total Due (including 15% VAT):**")

        

with col_billing2:

        st.write(f"{order_subtotal:,.2f} SAR")

        if is_authenticated:

            st.write(f"*{discounted_total:,.2f} SAR*")

        st.write(f"**{final_total_with_tax:,.2f} SAR**") 



    # =========================
    # Person 4: Checkout & Confirmation
    # =========================

    
    if st.button("Confirm Reservation"):

        if selected_details["Status"] != "Available":
            st.error(f"Sorry, this race is {selected_details['Status']}. You cannot book it.")

        else:
            st.success("Reservation Confirmed Successfully!")

            st.write("## Receipt")

            st.markdown(f"""
            <div class="receipt-box">
                <h3>F1 Ticket Reservation Receipt</h3>
                <p><b>Race:</b> {selected_race}</p>
                <p><b>Location:</b> {selected_details['Location']}</p>
                <p><b>Date:</b> {selected_details['Date']}</p>
                <p><b>Time:</b> {selected_details['Time']}</p>
                <p><b>Tickets:</b> {booking_user["Quantity"]}</p>
                <p><b>Subtotal:</b> {order_subtotal:.2f} SAR</p>
                <p><b>After Discount:</b> {discounted_total:.2f} SAR</p>
                <p><b>Final Total Including VAT:</b> {final_total_with_tax:.2f} SAR</p>
                <p><b>Status:</b> Confirmed</p>
            </div>
            """, unsafe_allow_html=True)