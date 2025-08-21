QUERY = """
query GetTop250Anime($page: Int = 1, $perPage: Int = 50) {
      Page(page: $page, perPage: $perPage) {
        pageInfo {
          total
          currentPage
          lastPage
          hasNextPage
          perPage
        }
        media(type: ANIME, sort: SCORE_DESC, isAdult: false) {
          id
          title {
            romaji
            english
            native
          }
          meanScore
          averageScore
          popularity
          favourites
          episodes
          duration
          status
          startDate {
            year
            month
            day
          }
          endDate {
            year
            month
            day
          }
          season
          seasonYear
          format
          genres
          studios {
            nodes {
              name
            }
          }
          coverImage {
            large
            medium
            color
          }
          bannerImage
          description(asHtml: false)
          siteUrl
          rankings {
            id
            rank
            type
            format
            year
            season
            allTime
            context
          }
        }
      }
    }
"""