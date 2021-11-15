"""
vitabot 3000
"""

import services.data as data_services

def main():
    """Main entrypoint"""
    food_service = data_services.food_data_service()
    print(food_service.get_unique_ids())

if __name__ == '__main__':
    main()
