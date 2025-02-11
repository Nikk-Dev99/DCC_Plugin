from flask import Flask, request, jsonify
import time
import sqlite3

app = Flask(__name__)

# Delay Function
def delayed_response(data, status_code=200):
    time.sleep(10)  # Simulated delay for testing
    return jsonify(data), status_code

def get_db():
    conn = sqlite3.connect("inventory.db")
    conn.row_factory = sqlite3.Row
    return conn

# API Endpoints

@app.route("/transform", methods=["POST"])
def transform():
    data = request.json
    print("Transform Data:", data)
    return delayed_response({"status": "success", "data": data})

@app.route("/translation", methods=["POST"])
def translation():
    data = request.json
    print("Translation Data:", data)
    return delayed_response({"status": "success", "data": data})

@app.route("/rotation", methods=["POST"])
def rotation():
    data = request.json
    print("Rotation Data:", data)
    return delayed_response({"status": "success", "data": data})

@app.route("/scale", methods=["POST"])
def scale():
    data = request.json
    print("Scale Data:", data)
    return delayed_response({"status": "success", "data": data})

@app.route("/file-path", methods=["GET"])
def file_path():
    project_path = request.args.get("projectpath", "false").lower() == "true"
    path = "/path/to/project/folder" if project_path else "/path/to/blender/file.blend"
    return delayed_response({"file_path": path})

@app.route("/add-item", methods=["POST"])
def add_item():
    try:
        data = request.json
        name = data.get("name")
        quantity = data.get("quantity")

        # Validation: Check if name or quantity is missing
        if not name or quantity is None:
            return delayed_response({"status": "error", "message": "Missing name or quantity"}, 400)

        # Validation: Ensure quantity is a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            return delayed_response({"status": "error", "message": "Quantity must be a positive integer"}, 400)

        conn = get_db()
        cursor = conn.cursor()

        # Check if the item already exists
        cursor.execute("SELECT * FROM inventory WHERE name = ?", (name,))
        if cursor.fetchone():
            return delayed_response({"status": "error", "message": "Item already exists"}, 400)

        # Insert the item into inventory
        cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()
        return delayed_response({"status": "success", "message": "Item added"})

    except Exception as e:
        return delayed_response({"status": "error", "message": str(e)}, 500)
    finally:
        conn.close()


@app.route("/remove-item", methods=["DELETE", "POST"])
def remove_item():
    try:
        data = request.json
        name = data.get("name")

        # Validation: Check if name is missing
        if not name:
            return delayed_response({"status": "error", "message": "Missing item name"}, 400)

        conn = get_db()
        cursor = conn.cursor()

        # Check if the item exists before deleting
        cursor.execute("SELECT * FROM inventory WHERE name = ?", (name,))
        item = cursor.fetchone()

        if not item:
            return delayed_response({"status": "error", "message": "Item not found in inventory"}, 404)

        # Delete the item
        cursor.execute("DELETE FROM inventory WHERE name = ?", (name,))
        conn.commit()

        return delayed_response({"status": "success", "message": "Item removed"})

    except Exception as e:
        return delayed_response({"status": "error", "message": str(e)}, 500)
    finally:
        conn.close()

@app.route("/update-quantity", methods=["PUT"])
def update_quantity():
    try:
        data = request.json
        name = data.get("name")
        quantity = data.get("quantity")

        if not name or quantity is None:
            return delayed_response({"status": "error", "message": "Missing name or quantity"}, 400)

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (quantity, name))
        if cursor.rowcount == 0:
            return delayed_response({"status": "error", "message": "Item not found"}, 404)

        conn.commit()
        return delayed_response({"status": "success", "message": "Quantity updated"})

    except Exception as e:
        return delayed_response({"status": "error", "message": str(e)}, 500)
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
