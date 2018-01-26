def format_csv(schedule):
    for week, schedule in schedule.items():
        print(f"{schedule.leader}, 0, {week}")
        for block, staffs in schedule.staffs.items():
            for staff in staffs:
                print(f"{staff}, {block}, {week}")
    pass
