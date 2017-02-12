from models import session, Team, Mentor, Skill


def calc_teams_in_room(room):
    return session.query(Team).filter(room == Team.room).count()


def get_teams_by_tech(tech):
    skill = session.query(Skill).filter(tech == Skill.name).one()
    teams_by_tech = {}
    teams_by_tech[skill.name] = []

    for team in skill.team:
        teams_by_tech[skill.name].append(team.name)

    return teams_by_tech


def add_skill(team, skills: list):
    team = session.query(Team).filter(Team.name == team).one()
    for s in skills:
        skill = session.query(Skill).filter(s == Skill.name).all()
        if skill not in team.skill:
            team.skill += skill

    session.commit()


def get_all_teams():
    return [team for team in session.query(Team).all()]


def add_mentor(name, description, picture):
    mentor = Mentor(name=name, description=description, picture=picture)
    session.add(mentor)
    session.commit()


def get_mentor_teams_info(mentor):
    mentor = session.query(Mentor).filter(Mentor.name == mentor).one()

    return {
        mentor.name: {
            'team_name': team.name,
            'team_id': team.id,
            'idea_description': team.idea_description,
            'repository': team.repository,
            'members_needed_desc': team.members_needed_desc,
            'room': team.room,
            'place': team.place,
            'skills': [skill.name for skill in team.skill]

            }
        for team in mentor.team
    }


def create_shcedule():
    pass


# print(get_teams_by_tech('Python'))
# print(get_mentor_teams_info('Антон Ненов'))
# add_mentor('Dinko', 'The border keeper', 'None')
# add_skill('Kappa', ['GO', 'Python'])
