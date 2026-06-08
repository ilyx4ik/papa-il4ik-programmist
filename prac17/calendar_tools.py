class UkrainianCalendar:
    def get_holiday_list(self):
        return [
            "01-01: Новий Рік",
            "24-08: День Незалежності",
            "01-10: День захисників і захисниць",
            "25-12: Різдво"
        ]

    def is_working_day(self, date_str):
        import datetime
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            return date_obj.weekday() < 5  
        except ValueError:
            return False
