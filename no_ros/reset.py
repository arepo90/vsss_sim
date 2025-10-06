import socket
import pickle
import sys

# ==============================================================================
# NOTE: These definitions MUST MATCH the ones in your other scripts!
# ==============================================================================

# Port configuration for the service
SIM_CONTROLLER_PORT = 10007 # From the TOPIC_PORTS dict in your other files

# Message class definitions needed to construct the request
class ObjData:
    def __init__(self, x=0.0, y=0.0, theta=0.0, vx=0.0, vy=0.0, w=0.0):
        self.x, self.y, self.theta = x, y, theta
        self.vx, self.vy, self.w = vx, vy, w

class FieldData:
    def __init__(self):
        self.ball = ObjData()
        # We only need the ball attribute for this specific reset command
        # but a full implementation would have all robots.

# ==============================================================================
# Client Logic
# ==============================================================================

def call_reset_service():
    """Creates and sends a reset request to the simulation."""
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Set a timeout so the script doesn't hang forever if the sim isn't running
        s.settimeout(2.0)

        # --- 1. Construct the Request ---
        # Create the message structure the service expects
        field_data = FieldData()

        # In simulation.py, a ball.x value of 999 is the special signal
        # for a default reset.
        field_data.ball.x = 999

        request_payload = {'settings': field_data}

        # --- 2. Send the Request ---
        try:
            print("Sending reset request to the simulation...")
            # Pickle the data and send it to the simulation's service port
            s.sendto(pickle.dumps(request_payload), ('localhost', SIM_CONTROLLER_PORT))

            # --- 3. Wait for the Response ---
            response_bytes, _ = s.recvfrom(1024)
            response_data = pickle.loads(response_bytes)

            # --- 4. Print the Result ---
            print("\n--- Service Response ---")
            print(f"Success: {response_data.get('success', 'N/A')}")
            print("------------------------")

        except socket.timeout:
            print("\nError: Request timed out. Is the simulation script running?")
        except ConnectionResetError:
             print("\nError: Connection reset. This can happen on some systems; try again.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == '__main__':
    call_reset_service()