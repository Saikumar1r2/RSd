import sqlite3

class Sample:
    def __init__(self, sample_id, sample_name, received_date):
        self.sample_id = sample_id
        self.sample_name = sample_name
        self.received_date = received_date

    def save(self):
        # Connect to SQLite database (or create it)
        conn = sqlite3.connect('lims.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS samples (
                sample_id TEXT PRIMARY KEY,
                sample_name TEXT,
                received_date TEXT
            )
        ''')

        # Insert sample data into the database
        cursor.execute('''
            INSERT INTO samples (sample_id, sample_name, received_date)
            VALUES (?, ?, ?)
        ''', (self.sample_id, self.sample_name, self.received_date))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_samples():
        # Fetch all sample records
        conn = sqlite3.connect('lims.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM samples')
        samples = cursor.fetchall()
        conn.close()
        return samples

# Example usage:
# Creating a new sample
sample1 = Sample("S001", "Blood Sample", "2025-04-26")
sample1.save()

# Fetch and display all samples
all_samples = Sample.get_all_samples()
for sample in all_samples:
    print(sample)
