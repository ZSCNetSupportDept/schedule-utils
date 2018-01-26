def format_sql(schedule, table):
    for week, schedule in schedule.items():
        print(f"UPDATE {table} SET `block`=0, `week`={week}, WHERE `name`={schedule.leader}")
        for block, staffs in schedule.staffs.items():
            for staff in staffs:
                print(f"UPDATE {table} SET `block`={block}, `week`={week} WHERE `name`='{staff}'")
    pass
