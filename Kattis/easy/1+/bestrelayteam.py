def get_best_team(sorted_runners):
    best_time = float("inf")
    dream_team = []
    for front_runner, start, warm in sorted_runners:
        running_time = float(start)
        team = [front_runner]
        for next_runner, start2, warm2 in sorted_runners:
            if (front_runner != next_runner) and len(team) < 4:
                running_time += float(warm2)
                team.append(next_runner)
        if running_time < best_time:
            best_time = running_time
            dream_team = team
    print(best_time)
    print('\n'.join(dream_team))

number_of_lines = int(input())
runners = []
for i in range(number_of_lines):
    runners.append(input().split())
runners.sort(key=lambda x: float(x[2]))
get_best_team(runners)