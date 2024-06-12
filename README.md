# Restaurant-Management-System

The RMS class encapsulates a simplified version of a restaurant management system, focusing on the interaction between the restaurant staff and the customers during the ordering process. This system is designed to operate within a text-based interface, enhanced by a graphical user interface (GUI) component using Tkinter for a more interactive experience. Below is a detailed summary of the class and its functionalities:

## Initialization and Attributes
Constructor (__init__): Initializes the restaurant with a name and a menu, both passed as arguments. The menu is expected to be a dictionary mapping dish names to their prices. Additionally, it initializes attributes for the total bill and the current user's order.
## User Interaction Methods
1] welcome_user: Greets the user by printing a welcome message with the restaurant's name.
2] take_order: Prompts the user to enter their order, storing it in the user_order attribute.
3] display_menu: Outputs the menu items along with their prices, formatted for readability.
4] preparing_order: Simulates the order preparation process, updating the total bill based on the selected dish. It includes a delay to mimic real-world processing times.
5] serve_order: Announces that the order is ready.
6] display_bill: Shows the total cost of the order.
7] verify_bill: Handles the payment process, allowing the user to pay the bill in installments until the full amount is covered. It also calculates and displays any changes made by the user.
## Order Handling
1] order_process: Orchestrates the entire order cycle, starting with welcoming the user, displaying the menu, taking the order, preparing and serving the order, displaying the bill, verifying payment, and finally thanking the user for their visit. It includes logic to handle invalid orders by repeating the process until a valid order is placed.
2] repeat_order: Provides an option for the user to place another order after the initial one has been processed. Similar to order_process, it handles menu display, order taking, and preparation but does not involve billing or payment verification.
## Integration with Tkinter GUI
The main execution block reads restaurant details (name, menu items, and prices) from sunlight.txt. It then creates an instance of the RMS class with these details.
A Tkinter window is set up to display the restaurant name and a button labeled "CLICK HERE TO ORDER". Clicking this button triggers the order_process method of the RMS instance, initiating the ordering process within the GUI.
## Summary
The RMS class represents a basic yet functional model of a restaurant ordering system, designed to simulate interactions between customers and staff. It incorporates essential elements such as menu display, order placement, preparation, billing, and payment verification. Integrating a Tkinter GUI offers a more engaging way for users to interact with the system compared to traditional command-line interfaces. This design could serve as a foundation for further development, adding features like inventory management, customer feedback collection, and real-time order status updates to enhance the simulation's realism and utility.
