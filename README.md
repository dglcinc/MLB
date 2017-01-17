# MLB
Mountain Lakes Bowling - Application for managing bowlers and schedules for the local league.

## MVP 1 (delivered)
Display read-only public version of file. Uses a minimal index.html and jpg of the Excel schedule. Published as S3 static website with CloudFront distribution and Route 53 vanity domain. No CloudFormation, all done via AWS console. Includes icon package for display on mobile devices and OSX/Windows/Android using [realfavicongenerator](http://realfavicongenerator.net).

## MVP 2
Display read-only public version of schedule for current week. Use Serverless Framework to deliver services with REST APIs powered by Lambda functions, store data in Dynamo DB, host website as static hosting on S3, with CloudFront distribution and Route 53 domain.
