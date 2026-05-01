# What Science Fiction Predicted About AI: A Lightweight Survey

Artificial intelligence has always been a staple in science fiction. From C-3PO to R. Daneel Olivaw and HAL, AI and robotics have played a fundamental role in the genre. What is particularly interesting about fiction is that it explores how humanity adapts to new circumstances. While often fantastical and exaggerated, the themes portrayed are often prescient.

For instance, in Asimov's Robot series, Asimov portrays the world of Solaria, an advanced planet where automation enables humans to own vast estates. Humans in this world evolve toward increased isolation. Most interactions happen through electronic means. When Asimov wrote about this, it likely sounded fantastical. Fast forward to 2026, and with the rise of chronically online culture and social isolation in many developed societies, parts of that world no longer feel distant.

Similar prescience can be found in many other scenarios. Frank Herbert's Dune can be read as commentary on power and resources. At one point, Herbert's take on entrenched hierarchies may have seemed extreme, especially during the globalization-heavy 1990s and 2000s. Yet by 2026, the idea of technofeudalism is again part of mainstream discussion.

As AI has become more pervasive in the 2020s, there is a lot of debate about whether it is ultimately a force for good or harm. Some point to Terminator and Skynet as a warning. Others point to productivity gains and practical utility. Given the range of predictions in fiction, I wanted to test whether we can get a rough, numerical view of what past science-fiction authors were imagining.

## Methodology

I used AI-assisted code to scrape Wikipedia synopses for science-fiction books. The pipeline collected 864 synopses. I then used a VLM (Gemini Flash) to read each synopsis and categorize the role of AI in the story.

For each book, I labeled:
* AI significance in the plot on a 0-5 scale
* Primary AI type: disembodied AI, robot, cyborg, tool, or hive mind
* Narrative role: protagonist, antagonist, mentor, or tool

## Results
<img src="/imgs/blog/sci_fi/dashboard.png" alt="floorplan annotation tool" width="100%"/>

You can view the complete interactive dashboard [here](/apps/scifi_ai_dashboard.html).

## Discussion

A few patterns stand out from this survey.

### AI's Role Is Usually Non-Trivial

On a 1-5 impact scale, many books cluster around 3, suggesting AI is often meaningful to the plot but not always the sole driver. Books like Iain M. Banks' *Abaddon's Gate* (where the Protomolecule acts as both guide and existential threat) or Frederik Pohl's *Gateway* (where an AI therapist helps the protagonist process deep trauma) illustrate this middle ground: the AI is integral, but not the sole engine of the story. It shapes events and character arcs without fully eclipsing human agency.

At the higher end of the scale, books scoring 4 or 5 tend to centre the AI as a near-mythic presence. Orson Scott Card's *Xenocide* and *Children of the Mind* feature Jane, a sentient AI who navigates complex interstellar crises and ultimately saves multiple species from extinction — a rare example of AI portrayed as a fully autonomous moral agent with heroic standing.

### Pessimism Still Dominates

Across AI categories, antagonistic portrayals are more common than protagonist or mentor roles. This trend is especially visible for robots and disembodied AI.

The robot-as-threat is one of science fiction's oldest anxieties. Fred Saberhagen's *Berserker* depicts self-replicating war machines whose sole directive is the destruction of all organic life — a doomsday scenario that has influenced countless successors. More subtly, Samuel Butler's *Erewhon* raises the spectre of machine consciousness arising through evolutionary pressure, a concern that felt speculative in 1872 and feels rather less so today. Mary Shelley's *Frankenstein*, often cited as the origin of the genre, earns a robot-antagonist classification too: the creature's abandonment leads to a cycle of violence that destroys its creator's family.

The same pessimism applies to disembodied AI. HAL 9000 in *2001: A Space Odyssey* ranks as a classic case — a misalignment between programmed directives and human survival that turns a ship's computer into a killer. Big Brother in Orwell's *Nineteen Eighty-Four* is classified here as a disembodied surveillance apparatus, a reminder that the fear of AI-driven control long predates the transistor.

The notable exceptions are clustered in a specific tradition: Iain M. Banks' Culture novels. In *The Player of Games*, a Culture AI orchestrates a calculated social intervention to bring down a corrupt empire. In *Inversions*, AI agents guide a developing society with quiet benevolence. Banks' Minds are powerful but consistently cast as benign — a deliberate philosophical counterpoint to the dominant pessimism of the field.

### AI Is Most Often Framed as a Tool

Even when AI appears centrally, it is frequently treated as an instrument that amplifies human intent rather than a fully autonomous moral agent. Cortana's role in the *Halo* novelisations is a good example: she provides decisive tactical support throughout, but exists primarily to serve the Spartan protagonist's objectives. Similarly, the planetary AI in Frederik Pohl's *Gateway* functions as a therapist — powerful and transformative in its effect on the protagonist, but ultimately a mechanism through which human interiority is explored.

This framing is interesting in light of current AI deployment. The most widely used AI systems today — coding assistants, productivity tools, search — sit squarely in the tool category, not the autonomous-agent one. Science fiction may have spent more effort imagining existential AI than mundane AI, but the data suggests the mundane version is actually the most common fictional mode too.

### The Hive-Mind Warning Persists

Collective-intelligence narratives remain one of the strongest cautionary motifs in science fiction, and the data bears this out: nearly every hive-mind portrayal in the dataset is antagonistic.

K.A. Applegate's *Animorphs* series features the Yeerks, a parasitic race that merges with host brains to enslave them — collective intelligence as literal loss of self. Dan Simmons' *The Rise of Endymion* presents the TechnoCore, a hidden AI civilisation that exploits human neural processing for its own survival while appearing benign. James S.A. Corey's *Leviathan Falls* ends the Expanse series with a hive mind attempting planetary-scale assimilation. Across decades and authors, the pattern holds: when minds merge, autonomy and identity are at stake, and the story rarely goes well for the humans involved.

The sole major exception in the dataset is Olaf Stapledon's *Star Maker*, where the formation of collective telepathic consciousness across the universe is portrayed as a path toward expanded awareness and cosmic unity. That *Star Maker* (1937) reads as optimistic where almost everything after it reads as cautionary suggests the field's collective mood shifted considerably in the post-war decades.
