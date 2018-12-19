(async function () {
    const axios = require('axios')

    const {
        DRONE_REPO_NAME,
        DRONE_COMMIT_MESSAGE,
        DRONE_COMMIT_BRANCH,
        DRONE_BUILD_EVENT,
        DRONE_COMMIT_AUTHOR,
        CI_BUILD_NUMBER,
        DRONE_BUILD_STATUS,
        DRONE_COMMIT_LINK,
        PLUGIN_API_URL
    } = process.env

    await axios.post(PLUGIN_API_URL,
        {
            'drone_repo_name': DRONE_REPO_NAME,
            'drone_commit_branch':DRONE_COMMIT_BRANCH,
            'drone_commit_author':DRONE_COMMIT_AUTHOR,
            'drone_commit_message':DRONE_COMMIT_MESSAGE,
            'drone_commit_buildevent':DRONE_BUILD_EVENT,
            'drone_commit_status':DRONE_BUILD_STATUS,
            'drone_commit_link':DRONE_COMMIT_LINK,
            'ci_build_number':CI_BUILD_NUMBER
        },
        {
            headers:
            {
                'Content-Type': 'application/json'
            }
        }
    ).catch(err => console.log(err))
})()