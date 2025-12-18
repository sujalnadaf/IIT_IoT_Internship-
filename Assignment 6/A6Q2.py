import mysql.connector
from mysql.connector import Error

try:
    # Your existing connection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="smart_agriculture",  # Change to smart_agriculture if needed
        use_pure=True
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Ask user for threshold
        try:
            threshold = float(input("Enter moisture threshold: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            exit(1)

        # Query to retrieve records
        query = """
            SELECT sensor_id, moisture_level, datetime
            FROM soil_moisture
            WHERE moisture_level < %s
            ORDER BY datetime DESC
        """
        cursor.execute(query, (threshold,))
        rows = cursor.fetchall()

        if rows:
            print(f"\nRecords with MoistureLevel < {threshold}:")
            for sensor_id, moisture, dt in rows:
                print(f"SensorID: {sensor_id}, MoistureLevel: {moisture}, DateTime: {dt}")
        else:
            print(f"No records found below threshold {threshold}.")

except Error as e:
    print(f"MySQL error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
