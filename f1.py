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
# Rahaf: Race Database
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
# =========================
# Adaptive CSS Styling
# =========================

st.markdown("""
<style>
/* Remove the hardcoded stApp background so Streamlit can control dark/light mode automatically */

.f1-header {
    /* Uses Streamlit's secondary background variable automatically */
    background: var(--secondary-background-color);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 25px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    text-align: center;
}

.f1-main-title {
    font-size: 42px;
    font-weight: 900;
    color: var(--text-color); /* Automatically switches black/white */
    margin-bottom: 5px;
}

.f1-subtitle {
    color: var(--text-color);
    opacity: 0.8;
    font-size: 18px;
}

.f1-card {
    background: var(--secondary-background-color);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 10px;
    min-height: 335px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.f1-round {
    color: var(--text-color);
    opacity: 0.6;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 1px;
}

.f1-country {
    color: var(--text-color);
    font-size: 28px;
    font-weight: 900;
    margin-top: 5px;
}

.f1-race-name {
    color: var(--text-color);
    opacity: 0.8;
    font-size: 13px;
    text-transform: uppercase;
    margin-top: 4px;
    min-height: 35px;
}

.f1-date {
    color: #d93829; /* F1 Red accent */
    font-size: 25px;
    font-weight: bold;
    margin-top: 14px;
}

.f1-info {
    color: var(--text-color);
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
    color: #71717a;
    font-weight: bold;
}

.center-section {
    max-width: 900px;
    margin: auto;
    text-align: center;
}

.payment-box {
    background: var(--secondary-background-color);
    padding: 24px;
    border-radius: 18px;
    border: 1px solid var(--border-color);
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    color: var(--text-color);
    text-align: center;
}

.receipt-wrapper {
    max-width: 1100px;
    margin: 25px auto;
}

[data-testid="stMetricValue"] {
    font-size: 24px;
}

[data-testid="stMetricLabel"] {
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Maram: Functions and Constants
# =========================

TICKET_TIERS = {
    "General Admission (Standard)": 1.0,
    "Grandstand Seating (Premium)": 1.5,
    "VIP Champions Club (Luxury)": 2.5
}

def calculate_total(cart_item, database):
    subtotal = 0
    race_name = cart_item["Race"]
    quantity = cart_item["Quantity"]

    ticket_type = cart_item.get("Ticket Type", "General Admission (Standard)")

    if race_name in database:
        base_unit_price = database[race_name]["Price"]
        multiplier = TICKET_TIERS.get(ticket_type, 1.0)
        subtotal = (base_unit_price * multiplier) * quantity

    return subtotal


apply_discount = lambda amount: amount * 0.85
apply_tax = lambda amount: amount * 1.15

VALID_MEMBERSHIP_CODES = ["F1CLUB2026", "POLEPOSITION", "VIPPASS"]

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
# Rahaf: Search Feature
# =========================

st.write("## Search for a Race")
search_feature = st.text_input("Enter race name, for example: British, Qatar, or Abu Dhabi").lower()

st.write("## 2026 Formula 1 Race Schedule")

# =========================
# Rana: Race Cards - Two per row
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
                    <div class="f1-info">💰 Starting from {details['Price']} SAR</div>
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
# Rana + Maram + Noura
# Reservation, Payment, Receipt
# =========================

if "selected_race" in st.session_state:

    selected_race = st.session_state["selected_race"]
    selected_details = st.session_state["selected_details"]

    st.write("---")

    left_space, center_col, right_space = st.columns([0.5, 3, 0.5])

    with center_col:

        st.markdown('<div class="center-section">', unsafe_allow_html=True)

        st.write("## Complete Your Reservation")

        st.write(f"🏁 **Selected Race:** {selected_race}")
        st.write(f"📍 **Location:** {selected_details['Location']}")
        st.write(f"📅 **Date:** {selected_details['Date']}")
        st.write(f"⏰ **Time:** {selected_details['Time']}")
        st.write(f"💰 **Base Price per Ticket:** {selected_details['Price']} SAR")
        st.write(f"🎟️ **Status:** {selected_details['Status']}")

        quantity = st.number_input(
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
            "Quantity": quantity,
            "Status": selected_details["Status"]
        }

        st.success("Your booking selection has been saved.")

        # =========================
        # Ticket Type Selection
        # =========================

        st.write("---")
        st.write("### 🎟️ Ticket Type & Experience")

        selected_tier = st.selectbox(
            "Choose your seating experience tier:",
            options=list(TICKET_TIERS.keys())
        )

        booking_user["Ticket Type"] = selected_tier

        tier_multiplier = TICKET_TIERS[selected_tier]
        tier_price = selected_details["Price"] * tier_multiplier

        st.write(f"**Selected Tier:** {selected_tier}")
        st.write(f"**Tier Price per Ticket:** {tier_price:,.2f} SAR")

        # =========================
        # Membership Authentication
        # =========================

        st.write("---")
        st.write("### 🔐 Membership Authentication")

        user_code = st.text_input(
            "Enter your F1 Club Membership ID or Promo Code:",
            placeholder="e.g., F1CLUB2026"
        ).strip().upper()

        order_subtotal = calculate_total(booking_user, races)

        is_authenticated = False

        if user_code:
            if user_code in VALID_MEMBERSHIP_CODES:
                discounted_total = apply_discount(order_subtotal)
                is_authenticated = True
                discount_status = "15% VIP Discount Applied"
                st.success("Membership authenticated! 15% VIP discount applied.")
            else:
                discounted_total = order_subtotal
                discount_status = "Invalid code - No discount applied"
                st.error("Invalid code. Please check your code or continue without a discount.")
        else:
            discounted_total = order_subtotal
            discount_status = "No Discount Applied"

        final_total_with_tax = apply_tax(discounted_total)

        # =========================
        # Final Payment Details
        # =========================

        st.write("### 💳 Final Payment Details")

        col_billing1, col_billing2 = st.columns(2)

        with col_billing1:
            st.write("**Selected Tier:**")
            st.write("**Tier Price per Ticket:**")
            st.write("**Base Subtotal:**")
            if is_authenticated:
                st.write("**Discounted Subtotal:**")
            st.write("**Total Due including 15% VAT:**")

        with col_billing2:
            st.write(selected_tier)
            st.write(f"{tier_price:,.2f} SAR")
            st.write(f"{order_subtotal:,.2f} SAR")
            if is_authenticated:
                st.write(f"{discounted_total:,.2f} SAR")
            st.write(f"**{final_total_with_tax:,.2f} SAR**")

        # =========================
        # Noura : Checkout & Confirmation
        # =========================

        if st.button("Confirm Reservation"):

            status = selected_details["Status"]

            if status != "Available":
                st.error(f"Sorry, this race is {status}. You cannot book it.")

            else:
                st.success("Reservation Confirmed Successfully!")

                st.write("### Receipt")

                st.markdown('<div class="receipt-wrapper">', unsafe_allow_html=True)

                with st.container(border=True):
                    st.markdown(f"#### {selected_race}")
                    st.caption("Official F1 Grand Prix Ticket")
                    st.write("")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown(f"**Location:** {races[selected_race]['Location']}")
                        st.markdown(f"**Tickets:** {quantity} {'Ticket' if quantity == 1 else 'Tickets'}")
                        st.markdown(f"**Ticket Tier:** {selected_tier}")

                    with col2:
                        st.markdown(f"**Date:** {races[selected_race]['Date']}")
                        st.markdown(f"**Time:** {races[selected_race]['Time']}")
                        st.markdown(f"**Tier Price:** {tier_price:,.2f} SAR")

                    st.write("")

                    m1, m2, m3 = st.columns(3)

                    m1.metric("Subtotal", f"{order_subtotal:,.1f} SAR")
                    m2.metric("After Discount", f"{discounted_total:,.1f} SAR")
                    m3.metric("Final Total (Incl. VAT)", f"{final_total_with_tax:,.1f} SAR")

                    st.write("")
                    st.caption("Thank you for booking with us. See you at the track.")

                st.markdown('</div>', unsafe_allow_html=True)

                receipt_text = f"""
F1 RESERVATION RECEIPT

Race: {selected_race}
Location: {races[selected_race]['Location']}
Date: {races[selected_race]['Date']} | Time: {races[selected_race]['Time']}
Quantity: {quantity} Tickets
Ticket Tier: {selected_tier}
Tier Price per Ticket: {tier_price:,.1f} SAR

Subtotal: {order_subtotal:,.1f} SAR
Discount: {discount_status}
Discounted Total: {discounted_total:,.1f} SAR
Final Total including VAT: {final_total_with_tax:,.1f} SAR

Status: Confirmed
"""

                st.download_button(
                    label="Download Receipt as Text",
                    data=receipt_text,
                    file_name=f"F1_Receipt_{selected_race.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

        st.markdown('</div>', unsafe_allow_html=True)
