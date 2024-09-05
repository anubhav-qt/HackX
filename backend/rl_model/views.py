from django.shortcuts import render, redirect
from .models import UserProgress
from .rl_model import Q_values, ACTIONS
import numpy as np
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def chart_data(request):
    # Simulate getting user state from progress data
    user = request.user
    state = get_user_state(user)

    # Choose action based on Q-values
    action_idx = np.argmax(Q_values[state])
    recommended_action = ACTIONS[action_idx]

    # Example data, replace with your actual data logic
    data = {
        'Open': np.random.randint(10, 50),
        'Bounce': np.random.randint(10, 50),
        'Unsubscribe': np.random.randint(10, 50),
    }

    return JsonResponse({'data': list(data.values())})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Example: Simulate getting user state from progress data
def get_user_state(user):
    # Here you would fetch the user’s performance from the database and derive a state.
    progress = UserProgress.objects.filter(user=user).last()

    if progress:
        if progress.score >= 80:
            return 2  # High performance
        elif progress.score >= 50:
            return 1  # Medium performance
        else:
            return 0  # Low performance
    return 0  # Default to low performance if no data


def recommend_content(user):
    # Get the user state
    state = get_user_state(user)

    # Choose action based on Q-values
    action_idx = np.argmax(Q_values[state])
    recommended_action = ACTIONS[action_idx]

    return recommended_action


# Main dashboard where recommendations are made
def user_dashboard(request):
    recommended_content = recommend_content(request.user)
    return render(request, 'dashboard.html', {'recommended_content': recommended_content})
