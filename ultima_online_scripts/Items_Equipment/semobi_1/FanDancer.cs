using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a fan dancer corpse" )]
	public class FanDancer : BaseCreature
	{

		[Constructable]
		public FanDancer() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			//BaseSoundID = #x####;

			Name = "Fan Dancer";
			Body = 247;
			
			SetStr( 315, 375 );
			SetDex( 200, 255 );
			SetInt( 20, 25 );

			SetHits( 350, 420 );
			SetMana( 20, 25 );

			SetDamage( 24, 44 );

			SetDamageType( ResistanceType.Physical, 100 );

			SetResistance( ResistanceType.Physical, 40, 60 );
			SetResistance( ResistanceType.Fire, 50, 70 );
			SetResistance( ResistanceType.Cold, 50, 70 );
			SetResistance( ResistanceType.Poison, 50, 70 );
			SetResistance( ResistanceType.Energy, 40, 60 );

			SetSkill( SkillName.MagicResist, 100.0, 110.0 );
			SetSkill( SkillName.Tactics, 100.0, 120.0 );
			SetSkill( SkillName.Wrestling, 85.0, 95.0 );
			SetSkill( SkillName.Anatomy, 85.0, 95.0 );

			Fame = 300;
			Karma = -300;
			
		 PackGem(); 
         PackGem(); 
         PackGold( 1000, 1300 ); 
         PackMagicItems( 1, 5 );
			// pack tessen items
			//pack OrigamiPaper
			//pack bonzai seed
		}
		 
      	public override bool BardImmune{ get{ return true; } }
		public override int TreasureMapLevel{ get{ return 3; } } 
		public override FoodType FavoriteFood{ get{ return FoodType.Meat; } }

                public FanDancer( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}
