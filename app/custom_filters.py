from django import template
from datetime import datetime

register = template.Library()

@register.filter
def countdown_weeks(target_date):
    diff = target_date - datetime.now().date()
    return diff.days // 7

@register.filter
def countdown_days(target_date):
    diff = target_date - datetime.now().date()
    return diff.days

@register.filter
def countdown_hours(target_date):
    diff = target_date - datetime.now().date()
    return diff.seconds // 3600

@register.filter
def countdown_minutes(target_date):
    diff = target_date - datetime.now().date()
    return (diff.seconds // 60) % 60

@register.filter
def countdown_seconds(target_date):
    diff = target_date - datetime.now().date()
    return diff.seconds % 60
