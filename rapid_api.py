import requests
import pandas as pd


def actors_get_all_filmography(nconst):
    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    querystring = {
        "nconst": nconst
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()['filmography']
    print(response.text)
    return None


def search_cast(tconst):
    url = "https://imdb8.p.rapidapi.com/title/get-top-cast"

    querystring = {
        "tconst": tconst
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except Exception as e:
        print(e)
        return None
    if response.status_code == 200:
        return response.json()
    print(response.text)
    return None


def get_base(tconst):
    url = "https://imdb8.p.rapidapi.com/title/get-base"

    querystring = {
        "tconst": tconst
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()['title']
    print(response.text)
    return None


def get_bio(nconst):
    url = "https://imdb8.p.rapidapi.com/actors/get-bio"

    querystring = {
        "nconst": nconst
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()['name']
    print(response.text)
    return None


if __name__ == "__main__":

    # headers
    headers = {
        'x-rapidapi-key': "2e105f8abemsh399ae1f76ff3374p1cfa28jsnacf91565fa2d",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    video_dict = {}

    # find out casts in Magnolia
    start_video = 'tt0175880'
    actors = search_cast(start_video)
    if actors:
        count = 0
        # find out movies they have acted
        for actor in actors:
            actor = actor[6:-1]
            print(actor)
            videos = actors_get_all_filmography(actor)
            if videos is None:
                continue

            # count actors in each movie
            for video in videos:
                video_id = video['id'][7:-1]
                if video_id not in video_dict:
                    video_dict[video_id] = [actor]
                else:
                    if actor not in video_dict[video_id]:
                        video_dict[video_id].append(actor)
            # count += 1
            # if count >= 3:
            #     break
    # store final results
    out_data = []

    video_count = 0

    result = {}
    for video_id in video_dict:
        #  get those movies which have at least two actors in Magnolia
        if len(video_dict[video_id]) >= 2:
            print(video_id, len(video_dict[video_id]), video_dict[video_id])

            # find out casts in those movies by movie ids
            actors = search_cast(video_id)
            if actors is None:
                continue
            result[video_id] = []
            # fetch those actors who did not in Magnolia
            for actor in actors:
                actor = actor[6:-1]
                if actor not in video_dict[video_id]:
                    result[video_id].append(actor)
            video_name = get_base(video_id)
            actors = result[video_id]

            #  get actors' names by ids
            actor_result = []
            #  get three of them
            if len(actors) > 2:
                actors = actors[:3]
            #  fetch actors' names
            for actor in actors:
                actor_name = get_bio(actor)
                if actor_name is not None:
                    actor_result.append(actor_name)

            out_data.append([video_name, ','.join(actor_result)])

            video_count += 1
            if video_count >= 30:
                break

    # output data in excel
    df = pd.DataFrame(out_data)
    df.to_excel('result.xlsx', header=['movie_title', 'actors'], index=None)
