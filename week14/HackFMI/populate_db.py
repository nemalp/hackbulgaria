import requests
from models import session, Skill, Team, Mentor


PUBLIC_TEAMS = requests.get('https://hackbulgaria.com/hackfmi/api/public-teams')
SKILLS = requests.get('https://hackbulgaria.com/hackfmi/api/skills')
MENTORS = requests.get('https://hackbulgaria.com/hackfmi/api/mentors')


def populate_skills(skills):
    for s in skills:
        skill = Skill(id=s['id'], name=s['name'])
        session.add(skill)
    session.commit()


def populate_teams(teams):
    for t in teams:
        team = Team(id=t['id'], name=t['name'],
                    idea_description=t['idea_description'],
                    repository=t['repository'],
                    need_more_members=t['need_more_members'],
                    room=t['room'], place=t['place'])

        if t['technologies_full']:
            for skill in t['technologies_full']:
                s = session.query(Skill).filter(
                    Skill.name == skill['name']).one()

                team.skill.append(s)

        session.add(team)
    session.commit()


def populate_mentors(mentors):
    for m in mentors:
        mentor = Mentor(id=m['id'], name=m['name'],
                        description=m['description'],
                        picture=m['picture'])

        for team in m['teams']:
                t = session.query(Team).filter(
                    Team.name == team['name']).one()

                mentor.team.append(t)

        session.add(mentor)
    session.commit()


def main():
    populate_skills(SKILLS.json())
    populate_teams(PUBLIC_TEAMS.json())
    populate_mentors(MENTORS.json())


if __name__ == '__main__':
    main()
