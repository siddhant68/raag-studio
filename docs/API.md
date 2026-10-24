# Local API

Start the server and open **http://127.0.0.1:8477/api/docs** for the generated OpenAPI reference.
The schema is at `/api/openapi.json`. Requests stay on the local machine unless an explicitly enabled
planner uses an external text service.

| Operation | Endpoint |
| --- | --- |
| Replan an existing song without rendering | `POST /api/songs/{id}/plan` |
| Create a song and queue its takes | `POST /api/songs` |
| List the library / fetch a song | `GET /api/songs`, `GET /api/songs/{id}` |
| New take or refinement round | `POST /api/songs/{id}/rounds` |
| Change controls / create plan revision | `PATCH /api/songs/{id}/controls` |
| Job status / cancellation | `GET /api/jobs/{id}`, `POST /api/jobs/{id}/cancel` |
| Progress stream | `GET /api/events` |
| Audio with range support | `GET /api/takes/{id}/audio` |
| Feedback / favourites | `POST /api/takes/{id}/feedback` |
| Create an export | `POST /api/takes/{id}/exports` |
| Runtime status | `GET /api/system` |
| User settings | `GET /api/settings`, `PUT /api/settings` |
| Musical vocabulary | `GET /api/genres`, `GET /api/instruments`, `GET /api/recipes` |
| Capability wording | `GET /api/capabilities` |

For an existing song, inspect an updated musical plan without consuming a new take. Set
`RAAG_SONG_ID` to that song's ID from the library/API:

```sh
curl "http://127.0.0.1:8477/api/songs/$RAAG_SONG_ID/plan" \
  -H 'Content-Type: application/json' \
  -d '{"brief":"A spacious bansuri at dawn with gentle tabla and no voices", "controls":{"voice":"instrumental","duration_s":120,"takes":1,"bpm":78}}'
```

The response includes the plan, compiler report and real planner identity. Use the OpenAPI request schemas for
round, feedback and export fields. Creation supports idempotency keys to avoid duplicate jobs on repeat submits.
Exact lyrics use `controls.lyrics_text`; see the [configuration guide](CONFIGURATION.md).

This API is designed for localhost. It is not an authenticated public service.
