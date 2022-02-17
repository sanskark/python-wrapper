from webcaller import ValorantAPI

if __name__ == "__main__":
    valorant = ValorantAPI()

    # print(valorant.get_agents())
    print(valorant.get_agent_by_uuid("5f8d3a7f-467b-97f3-062c-13acf203c006"))