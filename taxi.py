points = ["A", "B", "C", "D", "E", "F"]
n = int(input("Enter the number of taxi: "))
db = {}


def getting_taxi_detail_from_user():
    pick_point = input("Enter the pick point: ")
    drop_point = input("Enter the drop point: ")
    pickup_time = input("Enter the pickup time: ")

    return pick_point, drop_point, int(pickup_time)


def checking_all_point(pick_point, drop_point, pickup_time):
    filter_ = list(filter(lambda x: db[x]["free_time"] <= pickup_time, db))
    if len(filter_) == 0:
        return [False, "0"]

    sort_ = sorted(filter_, key=lambda x: db[x]["salary"])
    sort_ = sorted(sort_, key=lambda x: abs(ord(db[x]["point_at"]) - ord(pick_point)))

    return [True, sort_[0]]


def checking_single_point(pick_point, drop_point, pickup_time):
    filter_ = list(filter(lambda x: db[x]["point_at"] == pick_point and db[x]["free_time"] <= pickup_time, db))
    if len(filter_) == 0:
        return checking_all_point(pick_point, drop_point, pickup_time)

    sort_ = sorted(filter_, key=lambda x: db[x]["salary"])

    return [True, sort_[0]]


def book_taxi(process_id):
    pick_point, drop_point, pickup_time = getting_taxi_detail_from_user()
    decision, id = checking_single_point(pick_point, drop_point, pickup_time)

    if decision:
        db[id]["free_time"]=pickup_time
        pi_ti = abs(ord(db[id]["point_at"]) - ord(pick_point))
        dr_ti = abs(ord(drop_point) - ord(pick_point))
        distance_travel = pi_ti + dr_ti
        s = abs(ord(drop_point) - ord(pick_point)) * 15
        salary = 100 + ((s - 5) * 10)
        db[id]["salary"] += salary
        if db[id]["free_time"]==0:
            db[id]["free_time"] =  pickup_time  + distance_travel
        else:         db[id]["free_time"] = db[id]["free_time"] + distance_travel

        history = [process_id, process_id, pick_point, drop_point, pickup_time+pi_ti, distance_travel+pickup_time, salary]
        db[id]["point_at"] = drop_point
        v=db[id]["history"]
        v.append(history)
        db[id]["history"]=v
        print(f"Taxi can be allotted.\nTaxi {id} is allotted")


    else:
        free_ = sorted(db, key=lambda x: db[x]["free_time"])

        print(f"No taxi were available. Taxi-{free_[0]} is free at {db[free_[0]]['free_time']}")


def display_taxi_detail():
    for i in db:
        print(f"Taxi-{i}    Total Earnings: RS.{db[i]['salary']}")
        for j in db[i]["history"]:
            print(*j)


def creating_taxi():
    for i in range(1, n + 1):
        db[str(i)] = {
            "point_at": "A",
            "salary": 0,
            "free_time": 0,
            "history": []
        }


if __name__ == "__main__":
    creating_taxi()
    i = 1
    while True:
        d = input("0 for book taxi, 1 for display detail, other value for quit the program:  ")
        if d == "0":
            book_taxi(i)
        elif d == "1":
            display_taxi_detail()
        else:
            break

        i += 1
