{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
{% block extra_js %}.



function confirmDelete() {
    return confirm('Êtes-vous sûr de vouloir supprimer ?');
}