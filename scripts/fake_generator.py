#!/usr/bin/env python3

import uuid
import random
import pandas as pd
from datetime import datetime, timedelta


def generate_participant_id():
    return str(uuid.uuid4())


def generate_self_rated_data(participant_id, start_date, num_years):
    data = []
    for year in range(num_years):
        date_measured = start_date + timedelta(days=365 * year)
        data.append({
            "participant_id": participant_id,
            "date_measured": date_measured.isoformat(),
            "status": random.choice(["Excellent", "Good", "Fair", "Poor", None])
        })
    return data


def generate_measureables_data(participant_id, start_date, num_months):
    data = []
    for month in range(num_months):
        date_measured = start_date + timedelta(days=30 * month)
        data.append({
            "participant_id": participant_id,
            "date_measured": date_measured.isoformat(),
            "height": round(random.uniform(1.5, 2.2), 2),
            "weight": round(random.uniform(50, 200), 2),
            "blood_pressure": f"{random.randint(90, 140)}/{random.randint(60, 90)}",
            "bmi": round(random.uniform(18.5, 40), 2),
            "body_fat_percentage": round(random.uniform(10, 50), 2),
            "waist_circumference": round(random.uniform(60, 130), 2),
            "resting_heart_rate": random.randint(50, 100),
            "respiratory_rate": random.randint(12, 20),
            "oxygen_saturation": random.randint(95, 100),
            "fasting_blood_glucose": round(random.uniform(70, 130), 2),
            "cholesterol_level": round(random.uniform(150, 300), 2),
        })
    return data


def generate_sleep_data(participant_id, start_date, num_days):
    data = []
    for day in range(num_days):
        date_measured = start_date + timedelta(days=day)
        data.append({
            "participant_id": participant_id,
            "date_measured": date_measured.isoformat(),
            "sleep_hours": round(random.uniform(4, 12), 2),
            "sleep_stages": {
                "light": round(random.uniform(0, 5), 2),
                "deep": round(random.uniform(0, 5), 2),
                "REM": round(random.uniform(0, 5), 2),
            },
            "sleep_efficiency": round(random.uniform(50, 100), 2),
            "sleep_onset_latency": round(random.uniform(0, 60), 2),
            "number_of_awakenings": random.randint(0, 10),
            "time_spent_awake": round(random.uniform(0, 60), 2),
        })
    return data

import uuid
import random
from datetime import datetime, timedelta

def generate_osteology_data(participant_id, start_date, num_years):
    osteology_data = []
    fracture_types = ["Wrist", "Hip", "Spine", "Ankle", "Other"]

    for year in range(num_years):
        date_measured = start_date + timedelta(days=365 * year)
        num_fractures = random.randint(0, 3)
        fracture_history = []

        for _ in range(num_fractures):
            fracture_history.append({
                "fracture_type": random.choice(fracture_types),
                "fracture_date": (date_measured - timedelta(days=random.randint(0, 365))).isoformat(),
                "healing_duration": random.uniform(4, 12)
            })

        osteology_data.append({
            "participant_id": participant_id,
            "date_measured": date_measured.isoformat(),
            "density": random.uniform(0.5, 1.5),
            "bone_mineral_density": random.uniform(0.5, 1.5),
            "t_score": random.uniform(-3.0, 3.0),
            "z_score": random.uniform(-3.0, 3.0),
            "fracture_history": fracture_history,
            "bone_turnover_markers": {
                "blood": random.uniform(0.1, 10.0),
                "urine": random.uniform(0.1, 10.0)
            }
        })

    return osteology_data

def generate_hydration_data(participant_id, start_date, num_days):
    hydration_data = []
    for day in range(num_days):
        date_measured = start_date + timedelta(days=day)
        hydration_data.append({
            "participant_id": participant_id,
            "date_measured": date_measured.isoformat(),
            "water_intake_liters": random.uniform(1, 4),
            "hydration_level": random.choice(["Low", "Normal", "High"])
        })
    return hydration_data

def generate_oral_health_data(participant_id, start_date, num_years):
    oral_health_data = []
    for year in range(num_years):
        for month_offset in [0, 6]:
            date_measured = start_date + timedelta(days=30 * (year * 12 + month_offset))
            oral_health_data.append({
                "participant_id": participant_id,
                "date_measured": date_measured.isoformat(),
                "oral_health_status": {
                    "number_of_teeth_present": random.randint(0, 32),
                    "number_of_missing_teeth": random.randint(0, 32),
                    "tooth_decay": [
                        {
                            "tooth_number": random.randint(1, 32),
                            "severity": random.choice(["mild", "moderate", "severe"])
                        }
                        for _ in range(random.randint(0, 5))
                    ],
                    "periodontal_disease_status": random.choice(["healthy", "gingivitis", "periodontitis", None]),
                },
                "dental_imaging": [
                    {
                        "image_date": date_measured.isoformat(),
                        "image_type": random.choice(["xray", "ct", "mri"]),
                        "image_url": f"https://example.com/images/{participant_id}/oral_health/{year * 12 + month_offset}.jpg"
                    }
                ]
            })

    return oral_health_data


def save_data_to_parquet(data, filename):
    df = pd.DataFrame(data)
    df.to_parquet(filename, index=False)


def generate_and_save_data(num_participants, start_date):
    for i in range(num_participants):
        participant_id = generate_participant_id()

        self_rated_data = generate_self_rated_data(participant_id, start_date, 2)
        save_data_to_parquet(self_rated_data, f"data/self_rated_data_{participant_id}.parquet")

        measureables_data = generate_measureables_data(participant_id, start_date, 24)
        save_data_to_parquet(measureables_data, f"data/measureables_data_{participant_id}.parquet")

        sleep_data = generate_sleep_data(participant_id, start_date, 730)
        save_data_to_parquet(sleep_data, f"data/sleep_data_{participant_id}.parquet")

        osteology_data = generate_osteology_data(participant_id, start_date, 2)
        save_data_to_parquet(osteology_data, f"data/osteology_data_{participant_id}.parquet")

        hydration_data = generate_hydration_data(participant_id, start_date, 730)
        save_data_to_parquet(hydration_data, f"data/hydration_data_{participant_id}.parquet")

        oral_health_data = generate_oral_health_data(participant_id, start_date, 2)
        save_data_to_parquet(oral_health_data, f"data/oral_health_data_{participant_id}.parquet")

if __name__ == "__main__":
    num_participants = 100
    start_date = datetime(2020, 1, 1)
    generate_and_save_data(num_participants, start_date)
