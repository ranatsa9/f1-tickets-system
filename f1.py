
import streamlit as st

# =========================
# Person 1
# =========================

# Dictionary of the upcoming grand prix races

races = {
    "Spanish Grand Prix": {
        "Price": 400,
        "Location": "Circuit de Barcelona-Catalunya",
        "Time": "16:00",
        "Date": "2026-06-14",
        "Status": "Completed"
    },
    "Austrian Grand Prix": {
        "Price": 550,
        "Location": "Red Bull Ring, Spielberg",
        "Time": "16:00",
        "Date": "2026-06-28",
        "Status": "Full"
    },
    "British Grand Prix": {
        "Price": 750,
        "Location": "Silverstone Circuit",
        "Time": "17:00",
        "Date": "2026-07-05",
        "Status": "Available"
    },
    "Belgian Grand Prix": {
        "Price": 620,
        "Location": "Circuit de Spa-Francorchamps",
        "Time": "16:00",
        "Date": "2026-07-19",
        "Status": "Full"
    },
    "Hungarian Grand Prix": {
        "Price": 480,
        "Location": "Hungaroring, Budapest",
        "Time": "16:00",
        "Date": "2026-07-26",
        "Status": "Available"
    },
    "Dutch Grand Prix": {
        "Price": 580,
        "Location": "Circuit Zandvoort",
        "Time": "16:00",
        "Date": "2026-08-23",
        "Status": "Available"
    },
    "Italian Grand Prix": {
        "Price": 650,
        "Location": "Autodromo Nazionale Monza",
        "Time": "16:00",
        "Date": "2026-09-06",
        "Status": "Available"
    },
    "Azerbaijan Grand Prix": {
        "Price": 450,
        "Location": "Baku City Circuit",
        "Time": "14:00",
        "Date": "2026-09-26",
        "Status": "Available"
    },
    "Singapore Grand Prix": {
        "Price": 800,
        "Location": "Marina Bay Street Circuit",
        "Time": "15:00",
        "Date": "2026-10-11",
        "Status": "Full"
    },
    "United States Grand Prix": {
        "Price": 700,
        "Location": "Circuit of The Americas, Austin",
        "Time": "23:00",
        "Date": "2026-10-25",
        "Status": "Available"
    },
    "Mexican Grand Prix": {
        "Price": 500,
        "Location": "Autódromo Hermanos Rodríguez",
        "Time": "23:00",
        "Date": "2026-11-01",
        "Status": "Available"
    },
    "Abu Dhabi Grand Prix": {
        "Price": 850,
        "Location": "Yas Marina Circuit",
        "Time": "17:00",
        "Date": "2026-12-06",
        "Status": "Available"
    }
}


# =========================
# Main code - Welcome screen and UI
# =========================

st.title("F1 Ticket Reservation System")
st.subheader("Welcome to the Ultimate Racing Experience!")
st.write("Browse upcoming Grand Prix events, check ticket availability, and reserve your seats.")


# =========================
# Person 1: Search Feature
# =========================

st.write("## Search for a Race")
search_feature = st.text_input("Enter race name, for example: Austrian or Abu Dhabi").lower()

st.write("## Available Races Schedule")


# =========================
# Person 1 + Person 2: Browse and Reserve Button
# =========================

for race_name, details in races.items():

    # Search term if user typed in search
    if search_feature and search_feature not in race_name.lower():
        continue

    with st.container(border=True):

        # Status of race
        status = details["Status"]

        if status == "Available":
            status_display = "🟢 **Available to Book**"
        elif status == "Full":
            status_display = "🔴 **Sold Out / Full**"
        else:
            status_display = "⚫ **Race Completed**"

        # Race title and status
        st.markdown(f"### **{race_name}** — {status_display}")

        # Details layout
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"📍 **Location:** {details['Location']}")
            st.write(f"📅 **Date:** {details['Date']}")

        with col2:
            st.write(f"⏰ **Time:** {details['Time']}")
            st.write(f"💰 **Ticket Price:** {details['Price']} SAR")

        # =========================
        # Person 2: Reserve Button
        # =========================

        if details["Status"] == "Available":
            if st.button("🎟️ Reserve This Race", key=f"reserve_{race_name}"):
                st.session_state["selected_race"] = race_name
                st.session_state["selected_details"] = details

        elif details["Status"] == "Full":
            st.warning("This race is sold out. You cannot reserve tickets for it.")

        elif details["Status"] == "Completed":
            st.info("This race has already taken place. Booking is closed.")


# =========================
# Person 2: Reservation Form
# =========================

if "selected_race" in st.session_state:

    selected_race = st.session_state["selected_race"]
    selected_details = st.session_state["selected_details"]

    st.write("---")
    st.write("## Complete Your Reservation")

    st.write(f"🏁 **Selected Race:** {selected_race}")
    st.write(f"📍 **Location:** {selected_details['Location']}")
    st.write(f"📅 **Date:** {selected_details['Date']}")
    st.write(f"⏰ **Time:** {selected_details['Time']}")
    st.write(f"💰 **Price per Ticket:** {selected_details['Price']} SAR")

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

    st.write("### Booking Summary")
    st.write(f"🏁 **Race:** {booking_user['Race']}")
    st.write(f"📍 **Location:** {booking_user['Location']}")
    st.write(f"📅 **Date:** {booking_user['Date']}")
    st.write(f"⏰ **Time:** {booking_user['Time']}")
    st.write(f"🎟️ **Number of Tickets:** {booking_user['Quantity']}")
    st.write(f"💰 **Price per Ticket:** {booking_user['Price']} SAR")
# =========================
#  Person3: Calculations & Discounts
# =========================


def calculate_total(cart_item, database): 
    subtotal = 0 
    race_name = cart_item["Race"]
    quantity = cart_item["Quantity"]
    
    if race_name in database: 
        unit_price = database[race_name]['Price']
        subtotal = unit_price * quantity 
    return subtotal

apply_discount = lambda amount: amount * 0.85  # 15% discount
apply_tax = lambda amount: amount * 1.15       # 15% VAT

# Only execute if a race has been selected
if "selected_race" in st.session_state:
    
    st.write("---")
    st.write("### Membership & Offers")
    
    # Ask the user if they have a membership
    has_membership = st.checkbox("Do you have an exclusive F1 Club Membership?")

    # 1. Calculate the base subtotal
    order_subtotal = calculate_total(booking_user, races)

    # 2. Check membership status to apply discount conditionally
    if has_membership:
        discounted_total = apply_discount(order_subtotal)
        st.success(" 15% Membership discount applied!")
    else:
        discounted_total = order_subtotal  # No discount applied

    # 3. Apply VAT to the running total
    final_total_with_tax = apply_tax(discounted_total)

    # 4. Output the final details to the UI
    st.write("###  Final Payment Details")
    st.write(f"**Subtotal:** {order_subtotal:,.2f} SAR")
    
    if has_membership:
        st.write(f"**Discounted Subtotal:** {discounted_total:,.2f} SAR")
        
    st.write(f"**Total Due (including 15% VAT):** **{final_total_with_tax:,.2f} SAR**")


    
# =========================
#  Person4: Checkout & Confirmation
# =========================

if st.button("Confirm Reservation"):

    if selected_details["Status"] != "Available":
        st.error(f"Sorry, this race is {selected_details['Status']}. You cannot book it.")
    else:
        st.success("Reservation Confirmed Successfully!")

        st.write("### Receipt")

        st.info(f"""
Race: {selected_race}

Location: {races[selected_race]['Location']}

Date: {races[selected_race]['Date']}

Time: {races[selected_race]['Time']}

Tickets: {booking_user["Quantity"]}

Subtotal: {order_subtotal:.2f} SAR

After Discount: {discounted_total:.2f} SAR

Final Total (Including VAT): {final_total_with_tax:.2f} SAR

Status: Confirmed
""")