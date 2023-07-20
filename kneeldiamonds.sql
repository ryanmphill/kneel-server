
--Create the Tables
CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Types`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` NVARCHAR(160) NOT NULL,
    `price_multiplier` NUMERIC NOT NULL
);

CREATE TABLE `Orders` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`timestamp`  INTEGER NOT NULL,
	`metal_id` INTEGER NOT NULL,
	`size_id` INTEGER NOT NULL,
	`style_id` INTEGER NOT NULL,
	`type_id` INTEGER,
	FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
	FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`type_id`) REFERENCES `Types`(`id`)
);

-- Insert starter data
INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241);

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);

INSERT INTO `Types` VALUES (null, "Ring", 1);
INSERT INTO `Types` VALUES (null, "Earring", 2);
INSERT INTO `Types` VALUES (null, "Necklace", 4);

INSERT INTO `Orders` VALUES (null, 1684513128264, 1, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 1684513184661, 1, 1, 2, 2);
INSERT INTO `Orders` VALUES (null, 1684513263009, 1, 1, 3, 3);
INSERT INTO `Orders` VALUES (null, 1684513509513, 2, 2, 2, 1);
INSERT INTO `Orders` VALUES (null, 1684513527521, 3, 3, 3, 1);
INSERT INTO `Orders` VALUES (null, 1684513790680, 5, 5, 3, 2);
INSERT INTO `Orders` VALUES (null, 1684513830825, 1, 1, 2, 3);

SELECT * FROM Orders;

